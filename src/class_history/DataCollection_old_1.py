import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Temperature_Data:
    def __init__(self,dfs):
        years = []
        for i in dfs.keys(): # Stores all years as strings in a list to easily call in the dictionary
            years.append(i)
        self.years = years # Declare for as self to call in CLass
        self.dfs = dfs

    def collect_day_high(self,month,day): # This function collects all highs for a given day between 1960-2024
        temps = []
        day-=1                # Bc rows start at 0 subtract 1
        month = (month-1)*3   # Jump by threes to skip average and minimun columns
        
        for year in self.years:
            df = self.dfs[year]
            high = np.array(df.iloc[day,month])
            if np.isnan(high) == False:  # Checks to make sure Data is clean
                temps.append(high)
            elif np.isnan(high) == True:
                raise ValueError("Data was read as NaN")
            else:
                raise ValueError("Data was flagged as both a Nan and not a Nan.")
        temps = np.array(temps)
        return temps

    def plot_hist(self, data, title, bins=None):
        if bins == None: # If no custom bins were given this is default bin
            bins = np.linspace(np.min(data),np.max(data),np.size(data))
            
        plt.hist(data, bins, edgecolor='black')
        plt.xlabel('Temperature')
        plt.ylabel('# of Times')
        plt.title(title)
        plt.show()













        