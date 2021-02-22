# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 11:04:46 2021

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
import pandas as pd

def run_simulation_parallel(
        state,
        infection_prob,
        n_ticks_to_quarantine,
        parallel,
        timetable,
        name_of_run,
        n_internal_runs = 60,
        n_initial_infections = 50,
        n = 100000,
        n_random_infections = 0,
        save_output = False
    ):

    model = Sim(state)
    
    
    # a list of lists with parameter settings for each repetition
    params_experiment = [
        [
         infection_prob,
         n_initial_infections,
         n,
         n_random_infections,
         timetable,
         n_ticks_to_quarantine,
         1, # n_internal runs
         str(rep), # name of run
         False, # save output
         False, # display simulation
        ] for rep in range(n_internal_runs)]
    
    if parallel:
        results = Parallel(n_jobs=15)(map(delayed(model.run), params_experiment))
    else:
        results = [model.run(params) for params in params_experiment]
    
    dfs = [output["df"] for output in results]
    
    df = pd.concat(dfs)
    
    if save_output:
        output_file_name = "output_data/parallel_" + name_of_run + ".csv"
        df.to_csv(output_file_name, index = False)
    
    return df

