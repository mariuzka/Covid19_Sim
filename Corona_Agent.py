# -*- coding: utf-8 -*-

from Helper import *
from World import *
from Visualizer import *
from Agent import *
from Cell import *



########################################################################################################################

# agent class

########################################################################################################################

class Corona_Agent(
    Agent,
):
    max_agents_on_cell = int
    moving_prob = float

    def __init__(self):

        Agent.__init__(self)

        self.gender = int
        self.age = int
        self.infection = "s"                    # SEIR-state

        self.tick_of_infection = 0              # Tick der Infektion
        self.infection_duration_in_ticks = int
        self.tick_of_recovery = int

        self.cell_of_infection = None           # Zelle, auf der sich der Agent angesteckt hat (wird bei Infektion eingespeichert)

        self.target_cells = []                  # Zielzellen, zu der sich der Agent bewegen soll (meistens eine, außer beim Ausweichen)
        self.target_cell = None

        self.home_cell = Corona_Cell            # Zelle, auf der der Agent wohnt und immer wieder zurückkehrt

        self.activity = None                    # Bezeichnung (String) der aktuellen Aktivität. Wenn zu Hause, dann None.

        self.work_place = None                  # eine Zelle, die die Arbeitsstelle ist
        self.school = None                      # eine Zelle, die die Schule ist
        self.kindergarten = None                # a cell representing the agent's kindergarten

        self.fav_supermarkets = []              # Zellen, die die Lieblingssupermärkte sind

        self.ticks_doing_this_activity = None   # Anzahl der Ticks, die der Agent die aktuelle Aktivität bereits ausführt
        self.activity_len_in_ticks = None       # Anzahl der Ticks, die der Agent die aktuelle Aktivität ausführen soll

        self.group_dict = {"street": 0}
        
        self.shopping_prob = float
        self.go_for_a_walk_prob = float
        
        self.activities_done_today = []
        
        self.stay_at_home = False
        self.quarantine = False
        self.household_members = []
        
        

    def infect(self, tick, location_dependend_infection_prob_dict):

        # if agent is in any infectious state and if the agent is not the only one on his cell
        if self.infection in ["i", "a", "m"] and len(self.residence_cell.dict_of_residents) > 1:
            
            # get type of current location
            location = self.residence_cell.cell_type

            # get all agents on my cell in my group/room
            agents_in_my_group = [
                agent
                for agent in list(self.residence_cell.dict_of_residents.values())
                if agent.group_dict[location] == self.group_dict[location] and agent != self]

            # if there are other agents in the same group/room
            if len(agents_in_my_group) > 0:
                
                # pick one agent at random
                random_agent = random.choice(agents_in_my_group)
                
                # if the chosen agent is susbepicable
                if random_agent.infection == "s":
                    
                    # expose the selected agent with a certain probability
                    if random.random() < location_dependend_infection_prob_dict[location]:
                        random_agent.infection = "e"
                        random_agent.tick_of_infection = tick
                        random_agent.tick_of_exposure = tick
                        random_agent.cell_of_infection = self.residence_cell
                
                
    def update_status_of_infection(self, tick):
        
        # if agent has been exposed but is not yet infectious
        if self.infection == "e":
            
            if tick - self.tick_of_exposure >= self.duration_s:
                self.infection = "i"
                self.tick_of_infectivity = tick

        # if agent is currently infectious
        elif self.infection == "i":
            if tick - self.tick_of_infectivity > self.duration_i:
                self.tick_of_symptom_onset = tick
                
                # develop symptoms by an agent specific probability
                if random.random() < self.p_sym:
                    
                    # develop mild symptoms
                    self.infection = "m"
                    
                else:
                    # asymptomatic
                    self.infection = "a"
        
        # if agent is asymptomatic infected
        elif self.infection == "a":
            if tick - self.tick_of_symptom_onset > self.duration_r_a:
                self.infection = "r"
                self.tick_of_recovery = tick
        
        # if agent is infected with mild symptoms
        elif self.infection == "m":
            
            if tick - self.tick_of_symptom_onset > self.duration_r_m:
                self.infection = "r"
                self.tick_of_recovery = tick
            
    
    
    def decide_to_stay_at_home(self, tick, ticks_to_staying_at_home):
        """
        If an Agent has developed symptoms, he decides to stay at home after
        a given time span has passed since the onset of the symptoms. 
        It models the common behavior of people to stay at home when not feeling well.
        """
        
        # if agent has symptoms
        if self.infection in ["m"]:
            
            # wait until the number of ticks since symptom onset is higher than "ticks_to_staying_at_home"
            # could be 
            if tick - self.tick_of_symptom_onset >= ticks_to_staying_at_home:
                self.stay_at_home = True
        
        else:
            self.stay_at_home = False
        
            
    
    
    def decide_to_isolate_household(self, tick, ticks_to_isolate_household):
        """
        
        """
        # if one has symptoms and is not yet in quarantine
        if self.infection in ["m"] and not self.quarantine:
            
            # wait until some time has passed since symptom onset
            if tick - self.tick_of_symptom_onset >= ticks_to_isolate_household:
                
                # isolate household
                self.tick_of_quarantine = tick
                self.quarantine = True
                
                for member in self.household_members:
                    member.tick_of_quarantine = tick
                    member.quarantine = True
                    
        
        # if one is already in quarantine 
        if self.quarantine:
            if tick - self.tick_of_quarantine < 252: # 14 days * 18 daily ticks
                self.stay_at_home = True
            else:
                self.stay_at_home = False
                self.quarantine = False
            


    def initialize_activity(
            self,
            name_of_activity,       # Bezeichnung der Aktivität (String)
            target_cell,            # Zielzelle, an der die Aktivität ausgeführt wird
            activity_len_in_ticks,  # Die Aktivität wird solange an der Zielzelle ausgeführt
            overwrite = False,      # Wenn False, dann wird diese Aktivität ignoriert und die aktuelle einfach weitergeführt
                                    # Wenn der Agent zu Hause ist, dann ist die Aktivität auf "None" d.h. er kann neue
                                    # Aktivitäten empfangen
                                    # Wenn True, dann werden aktuelle Aktivitäten abgebrochen, egal ob der Agent zu Hause
                                    # ist oder nicht, und durch diese ersetzt

    ):
        """
        Initialisiert eine Aktivität. Mit der Funktion "do_acitivity" wird diese Aktivität bis der Agent wieder zu Hause ist,
        ausgeführt.
        Diese Funktion kann beispielsweise um eine gewisse Uhrzeit die Aktivität "Arbeit" initialisieren, welche dann
        in der folgenden Zeit von der Funktion "do_acitivity" ausgeführt wird.
        """
        
        if (not self.activity) or overwrite:
            
            self.activity = name_of_activity
            self.target_cell = target_cell
            self.activity_len_in_ticks = activity_len_in_ticks
            self.ticks_doing_this_activity = 0
            
            if name_of_activity not in self.activities_done_today:
                self.activities_done_today.append(name_of_activity)
            
            
    def do_activity(
            self,
            len_x_grid_dim,
            len_y_grid_dim,
            grid_as_matrix,
            torus,
    ):
        """
        Diese Funktion führt die initialisierte Aktivität aus. Die Trennung zwischen Initialisierung und Ausführung muss
        sein, damit um eine gewisse Uhrzeit die Aktivität gestartet werden kann, aber unabhängig von der Uhrzeit die Aktivität
        komplett ausgeführt werden kann.

        Das Ausführen der Aktivität besteht letztlich darin, zur angegeben Zielzelle zu gehen und sich dort für die
        angegebene Zeit aufzuhalten.
        """

        # Wenn eine Aktivität initialisiert wurde
        if self.activity:
            
            # Wenn die Zielzelle noch nicht erreicht wurde
            if self.target_cell:
                self.move_to_this_cell(self.target_cell)
                self.target_cell = None
             
            # Wenn der Agent die maximale Ausführungszeit noch nicht überschritten hat
            if self.ticks_doing_this_activity < self.activity_len_in_ticks:

                # Erhöhe die Zeit, die die Aktivität bereits ausgeführt wurde
                self.ticks_doing_this_activity += 1

            # Wenn die maximale Ausführungsdauer erreicht wurde
            else:

                # Aktivität abbrechen und nach Hause gehen
                self.move_to_this_cell(self.home_cell)
                self.activity = None
                self.ticks_doing_this_activity = None
                self.activity_len_in_ticks = None
                    
                    


########################################################################################################################

# cell class

########################################################################################################################

class Corona_Cell(Cell):
    def __init__(self, x_grid_pos, y_grid_pos):
        Cell.__init__(self, x_grid_pos, y_grid_pos)

        self.cell_type = "street"   # wenn ein Gebäude drauf gesetzt wird, dann wird der cell_type in den Gebäudetyp geändert
        self.building = None        # the building the cell belongs
        self.walkable = bool        # ob der Agent diese Zelle begehen kann/als Weg benutzen kann
        self.cumulative_number_of_residents = 0

        self.n_users = 0 # Anzahl der Bewohner/Schüler/Angestellte dieser Zelle
        self.n_groups = 0 # Anzahl der Wohnungen/Klassen/Abteilungen dieser Zelle
        self.groups = [[]] # Liste der Gruppen



########################################################################################################################

# building class

########################################################################################################################

class Building:

    """
    Ein Gebäude besteht aus mehreren Zellen.
    """
    def __init__(
            self,
            building_type,
            n_cells_x_dim=1,
            n_cells_y_dim=1,
    ):
        self.building_type = building_type
        self.n_cells_x_dim = n_cells_x_dim  # Größe des Gebäudes / Anzahl der Zellen auf der x-Achse
        self.n_cells_y_dim = n_cells_y_dim  # Größe des Gebäudes / Anzahl der Zellenauf der y-Achse
        self.cells = []                     # Zellen, aus denen das Gebäude besteht


    def build_it(
            self,
            building_x_origin,
            building_y_origin,
            grid_as_matrix,

    ):
        """
        Baut das Gebäude auf einer bestimmten Position auf dem Grid.
        Der Gebäude-Origin ist dabei die linke obere Ecke des Gebäudes.
        """
        for y in range(building_y_origin, building_y_origin + self.n_cells_y_dim):
            for x in range(building_x_origin, building_x_origin + self.n_cells_x_dim):

                # Gebäude-Typ der Zelle deklarieren
                grid_as_matrix[y][x].cell_type = self.building_type

                # Zelle unbegehbar machen
                grid_as_matrix[y][x].walkable = False

                # Konkretes Gebäude bei der Zelle einspeichern
                grid_as_matrix[y][x].building = self

                # Zelle als Bestandteil/Zelle beim Gebäude hinzufügen
                self.cells.append(grid_as_matrix[y][x])

        # den bebauten Zellen den Gebäudetyp einspeichern
        for cell in self.cells:
            cell.cell_type = self.building_type


    def build_it_on_random_position(
            self,
            grid_as_flat_list,
            grid_as_matrix,
    ):
        vacant_ground = [cell
                         for cell in grid_as_flat_list
                         if cell.cell_type == "street"]
        
        #building_ground = random.choice(vacant_ground)
        building_ground = vacant_ground[0]
        
        self.build_it(
            building_ground.x_grid_pos, 
            building_ground.y_grid_pos, 
            grid_as_matrix,
            )
        
        
        
        