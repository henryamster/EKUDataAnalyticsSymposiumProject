# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:02:01 2019

@author: henry
"""

import numpy as np

import csv

 

# get 10 flags/screens

screendata = open('rawTagData.csv', 'r')

 

# 1  Holiday Fixed

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

holiday_fixed = [int(x) for x in screen]

 

# 2  Holiday Roaming

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

holiday_roaming = [int(x) for x in screen]

 

# 3  Incement Weather Two Days Out

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

inclement_weather_two_days = [int(x) for x in screen]

 

# 4  Incement Weather One Day Out

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

inclement_weather_one_day = [int(x) for x in screen]

 

# 5  Optimal Weather Conditions

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

optimal_weather = [int(x) for x in screen]

 

# 6  Incement Weather

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

inclement_weather = [int(x) for x in screen]

 

# 7  Sportin Event Today

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

sporting_event = [int(x) for x in screen]

 

# 8  Community Event Today

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

community_event = [int(x) for x in screen]

 

# 9  Weekday

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

weekday = [int(x) for x in screen]

 

# 10 Weekend

screen = screendata.readline()

screen = (screen.strip('\n').split(','))

del screen[0] # drop first column from input record

del screen[0] # drop second column from the input record

weekend = [int(x) for x in screen]

 

# Close the file with Screen data

screendata.close()

 

 

# Read the Order Data for each Item and compute the daily average

datastream = open('raworderdata.csv', 'r')

#row = datastream.readline()

 

for row in datastream:

                data = (row.strip('\n').split(',') )

                item = data[0] # first column has the item description

               

                del data[0] # drop first column - item description

                del data[0] # drop second column

                data = [int(x) for x in data]

               

                dailyaverage = (sum(data) / len(data))

                print(item, '    Daily Average: ', dailyaverage)

 

                # check 10 different screens for meaningful change in Mean

               

                # Elementwise Multiplication

                a = np.array(data)

 

                b = np.array(holiday_fixed)

                elementwise = (a * b)

                print('Avg of Holiday Fixed:                   ', ( sum(elementwise) / sum(holiday_fixed)))

 

                b = np.array(holiday_roaming)

                elementwise = (a * b)

                print('Avg of Holiday Roaming:                 ', ( sum(elementwise) / sum(holiday_roaming)))

 

                b = np.array(inclement_weather_two_days)

                elementwise = (a * b)

                print('Avg of Inclement Weather Two Days Out:  ', ( sum(elementwise) / sum(inclement_weather_two_days)))

 

                b = np.array(inclement_weather_one_day)

                elementwise = (a * b)

                print('Avg of Inclement Weather One Day Out:   ', ( sum(elementwise) / sum(inclement_weather_one_day)))

 

                b = np.array(optimal_weather)

                elementwise = (a * b)

                print('Avg of Optimal Weather:                 ', ( sum(elementwise) / sum(optimal_weather)))

 

                b = np.array(inclement_weather)

                elementwise = (a * b)

                print('Avg of Inclement Weather:               ', ( sum(elementwise) / sum(inclement_weather)))

 

#             b = np.array(sporting_event) # I commented these two out because the flag is zero for all entries, causing division by zero

#             elementwise = (a * b)

#             print('Avg of Sporting Event:                  ', ( sum(elementwise) / sum(sporting_event)))

#

#             b = np.array(community_event)

#             elementwise = (a * b)

#             print('Avg of Community Event:                 ', ( sum(elementwise) / sum(community_event)))

 

                b = np.array(weekday)

                elementwise = (a * b)

                print('Avg of Weekday:                         ', ( sum(elementwise) / sum(weekday)))

 

                b = np.array(weekend)

                elementwise = (a * b)

                print('Avg of Weekend:                         ', ( sum(elementwise) / sum(weekend)))

 

                print()

 

# Close the data file

datastream.close()