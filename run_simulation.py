# -*- coding: utf-8 -*-

from Sim import *
from timetables import *
from def_get_params import *

import time
import math
import datetime as dt


# 1:  "Schleswig-Holstein",
# 2:  "Hamburg",
# 3:  "Lower Saxony",
# 4:  "Bremen",
# 5:  "North-Rhine-Westfalia",
# 6:  "Hessen",
# 7:  "Rheinland-Pfalz",
# 8:  "Baden-Wuerttemberg",
# 9:  "Bavaria",
# 10: "Saarland",
# 11: "Berlin",
# 12: "Brandenburg",
# 13: "Mecklenburg-Vorpommern",
# 14: "Saxony",
# 15: "Saxony-Anhalt",
# 16: "Thuringia",


params_hh = get_spotpy_params("important_outputs/params/LHS_BW_2021_01_20.csv")

STATE = 8
TIMETABLE = timetable_default
INFECTION_PROB = params_hh["infection_prob"]
N_INITIAL_INFECTIONS = 50
N = 10000
N_RANDOM_INFECTIONS = 0
N_TICKS_TO_QUARANTINE = params_hh["ticks_to_quarantine"]
N_INTERNAL_RUNS = 1
NAME_OF_RUN = "test12345"
SAVE_OUTPUT = False
DISPLAY_SIMULATION = True

params = [
     INFECTION_PROB,
     N_INITIAL_INFECTIONS,
     N,
     N_RANDOM_INFECTIONS,
     TIMETABLE,
     N_TICKS_TO_QUARANTINE,
     N_INTERNAL_RUNS,
     NAME_OF_RUN,
     SAVE_OUTPUT,
     DISPLAY_SIMULATION,
    ]

model = Sim(STATE)
output = model.run(params)