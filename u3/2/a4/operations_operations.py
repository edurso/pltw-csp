#!/usr/bin/env python3

# Eric D'Urso

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt

# READ DATAFRAME
df = pd.read_csv('operations.csv', header=0)

# CLEAN DATAFRAME
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)
#print(df['Value'])

# PROCESS & PLOT HONEY DATA SUM
all_honey = []
all_states = []
for state in df['State'].unique():
    honey_data = df[df['State'] == state].groupby('Year')['Value'] # collect data by state grouped by year
    all_honey.append(honey_data.mean()) # append the data to the list
    all_states.append(state) # append the state to the list of states
for i in range(len(all_states)): # add to plot for each state
    honey, state = all_honey[i], all_states[i] # get data for each state
    years = honey.keys() # get years from the keys of the data
    #print('Iteration {} | Honey: {}'.format(i, honey))
    plt.plot(years, honey, label=state) # throw it all on a graph
plt.ylabel('Honey Production') # label the honey
plt.xlabel('Year') # label the x axis with time
plt.title('Sum Honey Production Facilities Per State Over Time') # give graph a title
plt.show()

# PROCESS & BAR PLOT HONEY DATA AVERAGE
all_honey_avg = []
all_states_avg = []
for state in df['State'].unique():
    honey_data = df[df['State'] == state].groupby('Year')['Value'] # collect data by state grouped by year
    all_honey_avg.append(honey_data.mean()) # append the data to the list
    all_states_avg.append(state) # append the state to the list of states
for i in range(len(all_states_avg)): # add to plot for each state
    honey, state = all_honey_avg[i], all_states_avg[i] # get data for each state
    years = honey.keys() # get years from the keys of the data
    #print('Iteration {} | Honey: {}'.format(i, honey))
    plt.bar(years, honey, color='red') # throw it all on a graph
plt.ylabel('Honey Production Facilities') # label the honey
plt.xlabel('Year') # label the x axis with time
plt.title('Average Honey Production Facilities Per State Over Time') # give graph a title
plt.show()
