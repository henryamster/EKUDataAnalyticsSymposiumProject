# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:09:04 2019

@author: henryamsterfritz
https://henryfritz.xyz/
"""

import datetime
import numpy as np
import csv

#determine weekend status from datetime object
weekno = datetime.datetime.today().weekday()

if weekno<5:
    weekend = 0
else:
    weekend=1
    
holiday = input('Is today a holiday? if it is a set holiday (July 4th, December 25), please type 1, otherwise type 2, if it is not a holiday please type n: ')
if holiday == 1: 
     hd=1
elif holiday == 2: 
     hd=2
else: 
     hd=0      
  
     
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
    
   #append tags to tag array
tags=[]
if (hd ==1) :  
    tags.append(0)
elif (hd==2) :
    tags.append(1)
if (weekend==0):
    tags.append(8)
if (ideal==1):
    tags.append(4)  
if (inclement==1):
 tags.append(5)
if(daysOut=='2'):
 tags.append(2)        
if(daysOut=='1'):
 tags.append(3)   
if(sport==1):
 tags.append(6)
if(community==1):
 tags.append(7)
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
     

weights=[]  
order = []
 

index = 0
for items in orderDataContainer:
         
         #print(items, index)
         #https://en.wikipedia.org/wiki/Hadamard_product_(matrices)
         countSum= np.sum((tagDataContainer[4].astype(int) * orderDataContainer[index].astype(int)))
         countTrue = (tagDataContainer[4].astype(int) == 1).sum()
         weight = countSum/countTrue
         weights.append(weight)
         mean = np.average(orderDataContainer[index].astype(int))
         index= index+1
         print("mean: ", mean, "weight: ", weight  )
        # for qty in items:
         
        
         #order.append(mean.astype(int) * weights.astype(int))
         
             #print(qty)

    
    
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
     
     
