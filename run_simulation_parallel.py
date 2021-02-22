# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:24:31 2021

@author: ac135963
"""

from get_params import *
from def_run_simulation_parallel import *

params_by = get_spotpy_params("important_outputs/params/LHS_BY_2021_01_14.csv")

df = run_simulation_parallel(
    state = 9,
    infection_prob = params_by["infection_prob"],
    n_ticks_to_quarantine = params_by["ticks_to_quarantine"],
    parallel = True,
    timetable = timetable_default,
    name_of_run = "by_60_repr_test",
    save_output = True,
    )