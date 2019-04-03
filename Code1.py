# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:09:04 2019

@author: henryamsterfritz
https://henryfritz.xyz/
"""

import datetime
import numpy as np
import csv
import math 

#logic for query

weekno = datetime.datetime.today().weekday()

if weekno<5:
    weekend = 0
else:
    weekend=1
       
       #the date - to determine a holiday order and whether its a weekday or weekend
       #a switch statement will determine the tag map selection
       #whether inclement weather is expected for the order date
wx = input('Is the weather ideal, inclement, or normal?:  ')
if wx == 'ideal':
    ideal = 1
elif wx == 'inclement':
    inclement = 1
else:
    ideal = 0
    inclement = 0
    
fwx = input('If there is incoming inclement weather, how many days out is it? Please enter n if n/a: ')
if fwx == 2:
    daysOut = 2 
elif fwx == 1:
    daysOut = 1
else:
    daysOut = 0

    
       #whether a major sporting event is occuring
se = input('Is there a major sporting event today? y/n:  ')
if se == 'y':
    sport = 1
else:
    sport = 0
    
       #whether a major community event is occuring
ce = input('Is there a major community event today? y/n:  ')
if ce == 'y':
    community = 1
else:
    community = 0
    
 # query information complete

orderDataContainer = []
tagDataContainer = []
with open('RawOrderData.csv') as rawOrderData:
    reader = csv.reader(rawOrderData)
    count = 0
    for row in reader: 
     count = count+1
     orderDataContainer.append(np.array(row[:]))
   
with open('rawTagData.csv') as rawTagData:
    reader = csv.reader(rawTagData)
    count = 0
    for row in  reader:
     count = count+1
     tagDataContainer.append(np.array(row[:]))
     
#if (weekend==1):
   
weight=[]  
order = []
if (weekend==0):
    for ones in tagDataContainer[0].astype(int):
     countTrue = (tagDataContainer[0].astype(int) == 1).sum()
     countSum= np.sum(tagDataContainer[0].astype(int) * orderDataContainer[0].astype(int))
    weight= countSum/countTrue
    mean = np.average(orderDataContainer[0].astype(int))
    print(mean-weight)
    order.append(math.floor(mean*(1+weight)))
#if (ideal==1):
        
#if (inclement==1):
    
#if(daysOut=='2'):
            
#if(daysOut=='1'):
    
#if(sport==1):
    
#if(community==1):
    
    
    
#remember to use .astype(int) to cast np.arrays's values

#HOLIDAY FIXED - tagDataContainer[0]
#HOLIAY ROAMING - - tagDataContainer[1]
#INCLEMENT WEATHER TWO DAYS OUT - tagDataContainer[2]
#INCLEMENT WEATHER ONE DAY OUT - tagDataContainer[3]
#OPTIMAL WEATHER CONDITIONS - tagDataContainer[4]
#INCLEMENT WEATHER - tagDataContainer[5]
#SPORTING EVENT - tagDataContainer[6]
#COMMUNITY EVENT - tagDataContainer[7]
#WEEKDAY - tagDataContainer[8]
#WEEKEND - - tagDataContainer[9]
     
     