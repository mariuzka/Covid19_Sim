# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 12:31:45 2021

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
import pandas as pd


df = pd.read_csv("output_data/parallel_by_60_repr_test.csv")

#df_kalib = pd.read_csv("output_data/LHS_BY_2020_01_14.csv")
df_kalib = df_kalib.sort_values("like1", ascending = False).reset_index(drop = True)
best_df = df_kalib.iloc[0:1,:]
best_df["rank"] = best_df.index
best_df = pd.wide_to_long(best_df, ["simulation_"], i = "rank", j = "time")
best_df = best_df.reset_index()
best_df["day"] = best_df["time"]

sns.scatterplot(
    x="day", 
    y="empirical_cumulative_cases/100k", 
    data = df[df.day <= 100],
    label = "empirisch",
    color = "black"
    )
sns.lineplot(
    x="day", 
    y="simulation_", 
    data = best_df,
    label = ' "Kalibrierungsdurchgang", von welchem Parameter übernommen wurden (Mittelwert von 60 internen Reps.)',
    color = "red"
    )
sns.lineplot(
    x="day", 
    y="adj_cumulative_cases/100k", 
    data = df,
    label = "1. Replikation mit kalibrierten Parametern (Mittelwert von 60 internen Reps.)",
    color = "blue",
    ci = None
    )
sns.lineplot(
    x="day", 
    y="adj_cumulative_cases/100k", 
    data = df2,
    label = "2. Replikation mit kalibrierten Parametern (Mittelwert von 60 internen Reps.)",
    color = "purple",
    ci = None
    )


plt.legend()
plt.grid()
plt.title("Bayern")