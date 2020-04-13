#Please place your FUNCTION code for step 4 here.

#KMeansClustering_functions.py
#Odin Doolittle
#I modified Professor Cross's graphingKMeans function
#This file contains all functions for Part 4. 
#These functions create and graph iterations of KM

import numpy as np
import matplotlib.pyplot as plt
import math

#Functions
def openckdfile():
    #Takes no arguments. Opens the ckd file and interprets. It returns normal and
    #scaled values for glucose and hemoglobin and also their classification.
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification


def distance(CentHemo, DataHemo, CentGluc, DataGluc):
    #Takes an argument for a test hemoglobin and glucose and a data hemoglobin and 
    #glucose. It uses these values to calculate distance. It returns the distance. 
    dist = math.sqrt(((CentHemo-DataHemo)**2)+((CentGluc-DataGluc))**2)
    return dist

def Scaled(glucose, hemoglobin):
    #Takes glucose and hemoglobin arrays as arguments. Scales/normalizesS glucose and hemoglobin.
    #Returns the scaled glucose and scaled hemoglobin.
    glucose_scaled = (glucose - 70)/(420)
    hemoglobin_scaled = (hemoglobin - 3.1)/(14.7)
    return glucose_scaled, hemoglobin_scaled


def AssignToCentroid():
    #This function has no parameters. It assigns each data point in ckd to its 
    #closest Centroid. It returns a list of each assignment.
    ckd_index = 0
    Cent_Gluc = []
    Cent_Hemo = []
    Assignment_List = []
    for i in Centroids:
        Cent_Gluc.append(i[1])
        Cent_Hemo.append(i[0])
    for i in glucose:
        dist_list = []
        Cent_Count = 0
        gluc = glucose_scaled[ckd_index]
        hemo = hemoglobin_scaled[ckd_index]
        for i in Centroids:
            dist = distance(Cent_Hemo[Cent_Count], hemo, Cent_Gluc[Cent_Count], gluc)
            dist_list.append(dist)
            Cent_Count += 1
        ckd_index += 1
        smallest_dist = np.argmin(dist_list)
        Assignment_List.append(smallest_dist)
    return Assignment_List

def UpdateCentroids(K):
    #This function has a parameter K, the number of centroids. It uses the list of 
    #assigned centroids to find an average location and updates the centroid to 
    #this average location. It returns a list of the updated centroids. 
    Assignments = AssignToCentroid()
    Updated_Centroids = []
    count_K_List = 0
    for i in range(K):
        x = 0
        y = 0
        total = 0
        count_classifications_list = 0
        count_K_List += 1
        for i in Assignments:
            if i+1 == count_K_List:
        
                x += hemoglobin_scaled[count_classifications_list]
                y += glucose_scaled[count_classifications_list] 
                total += 1
            count_classifications_list += 1
        if total == 0:
            avgx = 0
            avgy = 0
        else:
            avgx = x/total
            avgy = y/total
        Updated_Centroids.append([avgx, avgy])
    return Updated_Centroids

def graphingKMeans(glucose, hemoglobin, assignment, centroids):
    #This function takes parameters glucose, hemoglobin, assignment, and centroids.
    #It plots the glucose and centroids with the color of their assigned centroid.
    #It plots the centroid. It has no return value.
    plt.figure()
    for i in range(assignment.max()+1):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i][0], centroids[i][1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

def Calculate_Accuracy(K):
    #This function, if K == 2, calculates true and false positives and negatives. 
    #It prints a label and the percentages of each. It has no return value.
    if K != 2:
        return False
    true_negative = 0
    false_positive = 0
    true_positive = 0
    false_negative = 0
    total = 0
    for i in range(len(Assignment_Array)):
        if classification[i] == 0 and Assignment_Array[i] == 0:
            true_negative += 1
            total += 1
        if classification[i] == 0 and Assignment_Array[i] == 1:
            false_positive += 1
            total += 1
        if classification[i] == 1 and Assignment_Array[i] == 1:
            true_positive += 1
            total += 1
        if classification[i] == 1 and Assignment_Array[i] == 0:
            false_negative += 1
            total += 1 
    print('True Positives Rate (Sensitivity) = ' + str((true_positive/total)*100) + '%') 
    print('False Positives Rate = ' + str((false_positive/total)*100) + '%') 
    print('True Negatives Rate (Specificity) = ' + str((true_negative/total)*100) + '%') 
    print('False Negatives Rate = ' + str((false_negative/total)*100) + '%') 

    


