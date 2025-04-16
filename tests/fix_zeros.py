from DataCollection import Temperature_Data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("cleandata.xlsx", sheet_name=None)
tp = Temperature_Data(data)
years = tp.years

def check_zeros(data):
    for i in range (data.size-1):
        if data[i] == 0:
            return True
    return False

def fix_zeros(df,year):
    months = np.arange(12) + 1
    for month in months: ### Goes through all months in a given year
        lows = tp.collect_month(month,year,"low")
        avgs = tp.collect_month(month,year,"average")
        highs = tp.collect_month(month,year,"high")
        tp.check_length_of_month(lows.size,month,year)
        tp.check_length_of_month(avgs.size,month,year)
        tp.check_length_of_month(highs.size,month,year)
        if check_zeros(lows):
            #print(f"Month = {month}. Year = {year}")
            for i in range(lows.size):
                if lows[i] == 0:
                    newlow = round(2*avgs[i] - highs[i],3)
                    lows[i] = newlow
                    assert lows[i] == newlow, f"The low was not changed for month = {month} and index = {i}."     
        pd_lows = np.append(lows,[float(np.nan)]*(31-lows.size))
        df.iloc[:,(3*month-1)] = pd_lows
    #print(f"Fixed zeros for {year}.")