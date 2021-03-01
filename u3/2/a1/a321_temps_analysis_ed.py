#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
temp_data = pd.read_csv("temperature_data.csv", header=0) # identify the header row

# Use matplotlib to make a line graph
plt.plot(temp_data['Year'], temp_data['Anomaly'], color='gray') # Plot Anomaly in a line graph
plt.plot(temp_data['Year'], temp_data['LOWESS'], color='blue') # Plot LOWESS in a line graph
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

# Use matplotlib to make a bar chart
plt.bar(temp_data['Year'], temp_data['Anomaly'], align='center', color='green')
plt.ylabel('Temperature Anomalies in Celsius')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()

# Calculate min, max, and avg anomaly and the corresponding min/max years
min_anomaly = temp_data['Anomaly'][0]
max_anomaly = temp_data['Anomaly'][0]
min_year = temp_data['Year'][0]
max_year = temp_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0

for i in range(0, len(temp_data['Anomaly'])):

    if (temp_data['Anomaly'][i] < min_anomaly):
        min_anomaly = temp_data['Anomaly'][i]
        min_year = temp_data['Year'][i]

    if (temp_data['Anomaly'][i] > max_anomaly):
        max_anomaly = temp_data['Anomaly'][i]
        max_year = temp_data['Year'][i]

    sum_anomaly = sum_anomaly + temp_data['Anomaly'][i]

avg_anomaly = sum_anomaly / len(temp_data['Anomaly'])

print('The maximum anomaly is: {} which occured in {}'.format(max_anomaly, max_year))
print('The minimum anomaly is: {} which occured in {}'.format(min_anomaly, min_year))
print('The average anomaly is: {:0.2f}'.format(avg_anomaly))
