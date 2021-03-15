#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

figure, (high, mid, low) = plt.subplots(3)

df = pd.read_csv('honey.csv', header=0)

'''

Step 11 - Pseudocode
1. replace comma values with empty space so they can become numbers
2. convert all string values to numeric values
3. drop any NaN

Step 13
Collects the sum ov all values up until this point from column value grouped by year

Step 19
The different graphs could have been divided by year (streches of a few year period)
or by region of the states.

'''

df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)

#print(df['Value'])

all_honey = []
all_states = []

for state in df['State'].unique():
    honey_data = df[df['State'] == state].groupby('Year')['Value'] # collect data by state grouped by year
    #print(state, honey_data.sum()) # print the state and its value
    all_honey.append(honey_data.sum()) # append the data to the list
    all_states.append(state) # append the state to the list of states
honey_sums = sorted([honey.sum() for honey in all_honey]) # sort by total honey production

def make_plot(sublist: list, title: str, axis: any) -> None:
    for i in range(len(all_states)): # add to plot for each state
        honey, state = all_honey[i], all_states[i] # get data for each state
        years = honey.keys() # get years from the keys of the data
        #print('Year = {}   |   Honey = {}'.format(years, honey))
        if honey.sum() in sublist:
            axis.plot(years, honey, label=state) # throw it all on a graph

    axis.set_ylabel('Honey Production') # label the honey
    axis.set_xlabel('Year') # label the x axis with time
    axis.set_title(title) # give graph a title
    axis.legend() # create a legend for each state

make_plot(honey_sums[:17], 'Small Producer Honey Production', low)
make_plot(honey_sums[17:34], 'Mid Producer Honey Production', mid)
make_plot(honey_sums[34:], 'Large Producer Honey Production', high)
plt.show()

