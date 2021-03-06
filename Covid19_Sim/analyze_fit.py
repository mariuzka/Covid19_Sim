# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:37:04 2021

@author: ac135963
"""

import pandas as pd
from sklearn.metrics import mean_squared_error
import math

df = pd.read_csv("good outputs/sim_exp_output_data_2021_01_28.csv")

# df = df[df.scenario == "standard"]

df = (df
      .loc[df.scenario == "standard",:]
      .loc[:,["state", "day", "empirical_cumulative_cases/100k", "adj_cumulative_cases/100k"]]
      .groupby(["state", "day"])
      .mean()
      .reset_index()
    )

list_rmse = []
for s in df.state.unique():
    condition = (df.state == s)
    
    mse = mean_squared_error(
        df.loc[condition, "empirical_cumulative_cases/100k"],
        df.loc[condition, "adj_cumulative_cases/100k"],
        )
    rmse = math.sqrt(mse)
    
    list_rmse.append(rmse)
    
df_rmse = pd.DataFrame(
    {"rmse": list_rmse,
     "state": df.state.unique(),
     })