
import pandas as pd
from pandas import read_html

#Reading table into python
filename = 'https://en.wikipedia.org/wiki/Estimates_of_historical_world_population'
tables = read_html(filename,
                   header=0,
                   index_col=0,
                   decimal='M')

table2 = tables[2]


#Eliminating all unnecessary data
table2.columns = ['census', 'prb', 'un', 'maddison',
                  'hyde', 'tanton', 'biraben', 'mj',
                  'thomlinson', 'durand', 'clark']

census = table2.census / 1e9
census

#Defining the beginning and end of the period
t_0 = census.index[0]
t_end = census.index[-1]
elapsed_time = t_end - t_0


#Finding growth rate of the population by first finding total population grouwth
p_0 = census[t_0]
p_end = census[t_end]
total_growth = p_end - p_0

annual_rate = total_growth / elapsed_time

#Creating a new time series to project future growth
results = pd.Series()
results[t_0] = p_0
for t in range(t_0, t_end + 8):
    results[t+1] = results[t] + annual_rate

#Thanos snaps and the population is cut in half in 2025
for t in range(t_end + 9):
  results[t_end + 9] = results[t_end + 8] / 2
results
