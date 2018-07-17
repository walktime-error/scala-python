# -*- coding: utf-8 -*-
import csv
from sklearn import tree
import random

"""
Created on Mon Jul 16 18:38:06 2018

This program takes a csv file as input and parses the columns into 
features and labels for machine learning algorithim.
This is a supervised learing classification algorithm to determine 
if the energy consumption at any point in time is high or average 

@author: Cynthia Khan
"""

features = []
labels = []
badLine = []

"""
open CSV input file and process each line
"""
with open('energy_consumption_data.csv') as csvDataFile:
  csvReader = csv.reader(csvDataFile, delimiter= ',')
  
  #skip header
  next(csvReader, None)
  for row in csvReader:
    if len(row) == 3:
      features.append(row[0:2])
      labels.append(row[2])
    else:
      badLine.append(row)
      
#Decision Tree Classifier Model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

date = random.randint(0,470)*5
energy = random.randint(0,50)

result = clf.predict([[date, energy]])

#result = result.tostring().decode("utf-8").replace(" ","").upper()

with open('msg.txt', 'w') as outfile:
    if (result == 'high'):
        outfile.write('Energy consumption is : HIGH \n'
                      + 'Do you want to switch off redundant devices?')
    else:
        outfile.write('Energy Consumption is : AVG')
      
#print(labels)