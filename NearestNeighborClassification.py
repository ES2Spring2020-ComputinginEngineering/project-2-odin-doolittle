#Please put your code for Step 2 and Step 3 in this file.
#NearestNeighborClassification.py
#Odin Doolittle
#I received some help from Professor Cross
#This contains functions and script for Parts 2 and 3. The scripts use data from 
#ckd file to determine if a test case does or does not have ckd.

import numpy as np
import math
import matplotlib.pyplot as plt
import random
from scipy import stats


# FUNCTIONS
def openckdfile():
    #Takes no arguments. Opens the ckd file and interprets. It returns raw and
    #scaled/normalized values for glucose and hemoglobin and also their classification.
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    hemoglobin_scaled = (hemoglobin - 3.1)/(14.7)
    glucose_scaled = (glucose - 70)/(420)
    return glucose, hemoglobin, classification, hemoglobin_scaled, glucose_scaled

def createTestCase():
    #Takes no arguments. It creates a random point within the range of known values
    #and scales them. It returns each variable for this test case. 
    newglucose = random.randint(70, 490)
    newhemoglobin = random.randint(31, 178)/10
    newglucose_scaled = (newglucose - 70)/(420)
    newhemoglobin_scaled = (newhemoglobin - 3.1)/(14.7)
    return newglucose, newhemoglobin, newglucose_scaled, newhemoglobin_scaled

def distance(TestHemo, DataHemo, TestGluc, DataGluc):
    #Takes an argument for a test hemoglobin and glucose and a data hemoglobin and 
    #glucose. It uses these values to calculate distance. It returns the distance. 
    dist = math.sqrt(((TestHemo-DataHemo)**2)+((TestGluc-DataGluc))**2)
    return dist

def calculateDistanceArray():
    #Calculates the distance between two scaled points. It returns each of these 
    #distances in a list.
    n = 0
    DistanceArray = []
    for i in classification:
        g = glucose_scaled[n]
        h = hemoglobin_scaled[n]
        DistanceArray.append(distance(newhemoglobin_scaled, h, newglucose_scaled, g))
        n += 1
    return DistanceArray

def nearestNeighborClassifier():
    #Takes no arguments. Chooses the index of the smallest distance in the distance
    #array. Returns the classification of this index.
    alldist = calculateDistanceArray()
    smallest_dist_index = np.argmin(alldist)
    return (classification[smallest_dist_index])
    
def kNearestNeighborClassifier():
    #Takes no arguments. Takes from the distance list the three shortest distances.
    #It returns the mode of the classification of these shortest distances.
    DistanceArray = calculateDistanceArray()
    SortedDistances = np.argsort(DistanceArray)
    k_indices = SortedDistances[:3]
    k_classifications = classification[k_indices]
    mode = stats.mode(k_classifications)
    if mode[0] == 0:
        return 0
    else: 
        return 1
# MAIN SCRIPT
newglucose, newhemoglobin, newglucose_scaled, newhemoglobin_scaled = createTestCase()
glucose, hemoglobin, classification, hemoglobin_scaled, glucose_scaled = openckdfile()        
print(kNearestNeighborClassifier())
            
plt.figure()
plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
plt.plot(newhemoglobin, newglucose, 'go', label = "TEST")
plt.xlabel("Hemoglobin")
plt.ylabel("Glucose")
plt.legend()
plt.show()
