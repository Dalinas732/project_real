import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Temperature_Data:
    def __init__(self,dfs):
        years = []
        
        for i in dfs.keys(): # Stores all years as strings in a list to easily call in the dictionary
            years.append(i)
            
        self.years = years # Declare as self to call in CLass
        self.dfs = dfs

    def check_length_of_month(self,count,month,year): # This function will help spot missing or incomplete data
        correct = None
        
        if month in {1,3,5,7,8,10,12}:
            correct = 31
            assert count == correct, f"Number of days in month = {month} year = {year}. {count} != correct {correct}."
        elif month in {4,6,9,11}:
            correct = 30
            assert count == correct, f"Number of days in month = {month} year = {year}. {count} != correct {correct}."
        elif month == 2:
            if int(year)%4 == 0:
                correct = 29
                assert count == correct, f"Number of days in month = {month} year = {year}. {count} != correct {correct}."
            else:
                correct = 28
                assert count == correct, f"Number of days in month = {month} year = {year}. {count} != correct {correct}."
        else:
            raise ValueError(f"Month = {month} was not read between 1-12. Year = {year}.")
        
    def collect_month(self,month,year,mode=None): ###!!! Will not handle NaNs correctly atm !!!####
        if isinstance(year, str):                 ### It will simply ignore them and move on
            pass
        elif isinstance(year,int):
            year = str(year)
        else:
            raise ValueError("Year type() is not string or int.")

        index = None
        if mode == None:
            raise ValueError("Must choose high, average, or low for data collection.")
        if mode == "high" or mode == 0:
            index = 3*(month-1)   # Jump by threes to skip average and minimun columns
        elif mode == "average" or mode == 1:
             index = 3*month - 2   # Only looks at average column for a given month
        elif mode == "low" or mode == 2:
            index = 3*month - 1 # Redfined for the minimum column
        else:
            raise ValueError("Mode not selected correctly.")
            
        df = self.dfs[year]
        temps_array = np.array(df.iloc[:,index],dtype=float)
        temps_list = []
        day = 1
        for temps in temps_array:
            if np.isnan(temps) == False:  # Checks to make sure Data is clean
                temps_list.append(temps)
            elif np.isnan(temps) == True and day <= 28:
                print(f"Warning: Read NaN in month={month} year = {year}.") ### Does not raise error
            #elif np.isnan(temps) == True and day >= 30 and month != 2:
             #   print(f"Warning: Read NaN in month={month} year = {year}.") ### Does not raise error
            #else:
                #raise ValueError(f"Value was not a float or a NaN. Month = {month} year = {year}.")
            day+=1
        temps = np.array(temps_list,dtype=float)
        return temps
        
    def collect_day(self,month,day,mode=None): # This function collects all highs for a given day between 1960-2024
        index = None
        assert day <= 31, "Input for day cannot be above 31."
        
        if mode == None:
            raise ValueError("Must choose high, average, or low for data collection.")
        if mode == "high" or mode == 0:
            index = 3*(month-1)   # Jump by threes to skip average and minimun columns
        elif mode == "average" or mode == 1:
             index = 3*month - 2   # Only looks at average column for a given month
        elif mode == "low" or mode == 2:
            index = 3*month - 1 # Redfined for the minimum column
        else:
            raise ValueError("Mode not selected correctly.")
            
        temps_list = []
        day_index= day - 1       # Bc rows start at 0 subtract 1
        
        for year in self.years:
            df = self.dfs[year]
            temps = np.array(df.iloc[day_index,index])
            if np.isnan(temps) == False:  # Checks to make sure Data is clean
                temps_list.append(temps)
            elif np.isnan(temps) == True:
                raise ValueError("Data was read as NaN.")
            else:
                raise ValueError("Data was flagged as both a Nan and not a Nan.")
                
        temps_array = np.array(temps_list,dtype=float)
        return temps_array
        
    def plot_hist(self, data, title = "Title", bins=None):
        if bins == None: # If no custom bins were given this is default bin
            bins = np.linspace(np.min(data),np.max(data),np.size(data))
            
        plt.hist(data, bins, edgecolor='black')
        plt.xlabel('Temperature')
        plt.ylabel('# of Times')
        plt.title(title)
        plt.show()













        
