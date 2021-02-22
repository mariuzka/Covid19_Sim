# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:27:22 2021

@author: ac135963
"""

import pandas as pd


def get_spotpy_params(path_to_spotpy_df):
    df = pd.read_csv(path_to_spotpy_df)
    df = df.sort_values("like1", ascending = False).reset_index(drop = True)
    ticks_to_quarantine = df.loc[0, "parn_ticks_to_quarantine"]
    infection_prob = df.loc[0, "parinfection_prob"]
    
    params = {
        "infection_prob":infection_prob,
        "ticks_to_quarantine": ticks_to_quarantine,
        }
    
    print(path_to_spotpy_df)
    print("RMSE:", df.loc[0, "like1"])
    print(params)
    
    return params