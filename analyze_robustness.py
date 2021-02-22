# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:47:02 2021

@author: ac135963
"""
import pandas as pd
import seaborn as sns
import statsmodels.formula.api as sm
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

dfs = []
rmse = []
n_colleagues = []

folder = "output_data/"
for i in range(2, 19, 2):
    file = folder + "output_n_colleagues_" + str(i) + ".csv"
    df = pd.read_csv(file)
    df["n_colleagues"] = i
    dfs.append(df)
    
    rmse.append(
        mean_squared_error(
            df["empirical_cumulative_cases/100k"], 
            df["adj_cumulative_cases/100k"],
            squared=False)
        )
    n_colleagues.append(i)
    

df = pd.concat(dfs)
df_lastday = df[df["day"] == 99]
df_lastday["adj_cumulative_cases_100k"] = df_lastday["adj_cumulative_cases/100k"]


plt.plot(n_colleagues, rmse)
plt.ylim(0,50)
plt.title("goodness of fit by number of colleagues")
plt.ylabel("Root mean squared error")
plt.xlabel("n colleagues")
#plt.grid()

a = 0.75
sns.set_style("whitegrid")
sns.lineplot(
    x = "day",
    y = "adj_cumulative_cases/100k",
    hue = "n_colleagues",
    data = df[df.n_colleagues.isin([2,4,6,8,12,14,16,18])],
    ci = None,
    palette=sns.color_palette("bright", n_colors=8),
    alpha = a,
    )
sns.lineplot(
    x = "day",
    y = "adj_cumulative_cases/100k",
    data = df[df.n_colleagues == 10],
    color = "black",
    linewidth = 2,
    label = "10",
    )
sns.scatterplot(
    x = "day",
    y = "empirical_cumulative_cases/100k",
    data = df[(df.run == 0) & (df.n_colleagues == 2)],
    color = "black",
    label = "reality",
    )




sns.boxplot(
    x = "n_colleagues",
    y = "adj_cumulative_cases/100k",
    data = df_lastday
    )
plt.ylabel("adj_cumulative_cases/100k at day 100")
#plt.xlabel("n_colleagues")

sns.regplot(
    x = "n_colleagues",
    y = "adj_cumulative_cases/100k",
    data = df_lastday,
    x_jitter=.25,
    )
plt.ylabel("adj_cumulative_cases/100k at day 100")


lm = sm.ols(
    formula="adj_cumulative_cases_100k ~ n_colleagues", 
    data=df_lastday,
).fit()

lm.summary()
