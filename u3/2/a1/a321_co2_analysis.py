#!/usr/bin/env python3

# Eric D'Urso
# Nick DaSilva
# Raymond Mei
# Zack Wilk

import matplotlib.pyplot as plt
import pandas as pd
import math

# Load in the data with read_csv()
co2_data = pd.read_csv("co2_data.csv", header=0) # identify the header row
print(co2_data)
co2_data['Average'] = co2_data['Average'].replace(-99.99, math.nan)
print(co2_data)
co2_data.dropna(subset=['Average'], inplace=True)
print(co2_data)

# Use matplotlib to make a line graph
plt.plot(co2_data['decimal_year'], co2_data['Average'], color='pink') # Plot Average in a line graph
plt.ylabel('CO2 Levels (ppm)')
plt.xlabel('Years')
plt.title('Change in Temperatures')
plt.show()
