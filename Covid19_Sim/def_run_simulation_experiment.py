# -*- coding: utf-8 -*-

"""
Created on Mon Aug 31 17:20:04 2020

@author: ac135963
"""

from Sim import *
from matplotlib import pyplot as plt
import seaborn as sns
import time
import math
import datetime as dt
from timetables import *
from joblib import Parallel, delayed
import os


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

def run_simulation_experiment(
        state,
        infection_prob,
        n_ticks_to_quarantine,
        parallel,
        n_internal_runs = 60,
        n_initial_infections = 50,
        n = 100000,
        n_random_infections = 0,
        save_output = True,
        display_simulation = False,
    ):

    model = Sim(state)
    
    # list of all timetables + a scenario name
    timetables = [
        (timetable_default, "standard"),
        (timetable_no_homeoffice, "no_homeoffice"),
        (timetable_no_reduction_of_work, "no_reduction_of_work"),
        (timetable_no_quarantine, "no_quarantine"),
        (timetable_open_kitas, "open_kitas"),
        (timetable_open_schools, "open_schools"),
        (timetable_open_schools_kitas, "open_schools_kitas"),
        (timetable_open_universities, "open_universities"),
        (timetable_open_education, "open_education"),
        ]
    
    # a list of lists with parameter settings for each timetable/scenario
    params_experiment = [
        [
         infection_prob,
         n_initial_infections,
         n,
         n_random_infections,
         timetable[0],
         n_ticks_to_quarantine,
         n_internal_runs,
         timetable[1] + "_" + str(state), # name of scenario/run
         save_output,
         display_simulation,
        ] for timetable in timetables]
    
    if parallel:
        results = Parallel(n_jobs=10)(map(delayed(model.run), params_experiment))
    else:
        results = [model.run(params) for params in params_experiment]
    
    return results
