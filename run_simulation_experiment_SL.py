# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 15:57:49 2020

@author: ac135963
"""

from build_simulation import *
from matplotlib import pyplot as plt
import seaborn as sns
import time
import math
import datetime as dt
from timetables import *
from joblib import Parallel, delayed
from def_run_simulation_experiment import *
from get_params import *

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

spotpy_params = get_spotpy_params("important_outputs/params/LHS_SAAR_2021_01_20.csv")

results = run_simulation_experiment(
    state = 10,
    infection_prob = spotpy_params["infection_prob"],
    n_ticks_to_quarantine = spotpy_params["ticks_to_quarantine"],
    parallel = True,
    )