#!/usr/bin/env python3

# Eric D'Urso

'''

ANSWERS TO ASSIGNMENT QUESTIONS

Step 11 - Pseudocode
1. replace comma values with empty space so they can become numbers
2. convert all string values to numeric values
3. drop any NaN

Step 13
Collects the sum ov all values up until this point from column value grouped by year

Step 19
The different graphs could have been divided by year (streches of a few year period)
or by region of the states.

Step 23
The benefit of manually validating some of the data in a spreadsheet software is 
that is assures us that the data processing algorithm is working correctly.

Step 26
The data does not appear to correlate to the problem with bee colonies in the United States
because the rate at which honey production is increasing, indicating that the amount of 
honey/bees is increasing as well.

Step 30
The operational facilities are increasing with the honey, indicating that natural honey 
production is being facilitated and is improving as a result as seen by the honey 
production graphs.

Step 34
The new data contradicts my original analysis, but supports the original problem of 
decreasing honey bee populations. The new data seems to indicate a major drop in the 
bee population between 1997 and 2002, after which the population rebounds and starts 
to stedily increase.

'''

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt

# READ DATAFRAME
df = pd.read_csv('honey.csv', header=0)

# CLEAN DATAFRAME
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df.dropna(subset=['Value'], inplace=True)
#print(df['Value'])

# PROCESS HONEY DATA SUM
all_honey = []
all_states = []
for state in df['State'].unique():
    honey_data = df[df['State'] == state].groupby('Year')['Value'] # collect data by state grouped by year
    #print(state, honey_data.sum()) # print the state and its value
    all_honey.append(honey_data.sum()) # append the data to the list
    all_states.append(state) # append the state to the list of states
honey_sums = sorted([honey.sum() for honey in all_honey]) # sort by total honey production

# SUBPLOT GRAPH FUNCTION
figure, (high, mid, low) = plt.subplots(1, 3)
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
    axis.legend(loc='center right', fontsize='small', bbox_to_anchor=(1.1, 0.5)) # create a legend for each state

# PLOT 3 HONEY SUM GRAPHS
make_plot(honey_sums[:17], 'Small Producer Honey Production', low)
make_plot(honey_sums[17:34], 'Mid Producer Honey Production', mid)
make_plot(honey_sums[34:], 'Large Producer Honey Production', high)
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
plt.ylabel('Honey Production') # label the honey
plt.xlabel('Year') # label the x axis with time
plt.title('Average Honey Production Per State Over Time') # give graph a title
plt.show()
