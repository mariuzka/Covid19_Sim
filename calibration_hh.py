# -*- coding: utf-8 -*-

from build_simulation import *
from timetables import *
from def_calibration import *

import pandas as pd
import spotpy
import time

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

###############################################################################   

state_calibration(
    state = 2,
    n_initial_infections = 50,
    n = 100000,
    timetable = timetable_default,
    n_internal_runs = 60,
    n_calibration_runs = 180,
    output_file_path = "output_data/LHS_HH_2021_01_22",
    name_of_run = "kalib_hh",
    parallel = True,
    )
