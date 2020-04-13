Odin Doolittle
Project 2 README

Files:
-NearestNeighborClassification.py
	- Contains functions to find the classification of a test point based on its 		nearest neighbor and kNearest neighbor.
	- Graphs all ckd points and test points.
-KMeansClustering_functions.py
	- Contains functions to assign a set of points to a randomly generated centroid. 	It also contains a function to update the random centroid based on the average 		location of its assigned points.
	- Also holds graphing function to graph centroids and their points.
-KMeansClustering_driver.py
	- Iterates functions from functions file and defines variables and generates 		random centroid.

Usage:
-NearestNeighnorClassification
	-Simply run the file or plug in custom points where the random generator would.

-KMeansClustering_functions.py
	-requires no action

-KMeansClustering_driver.py
	-Choose a starting K-value. Replace ckd file with custom file if desired. Run 		script.

Design of KMeansClusteringAlgorithm:

Custom functions

-Distance
	-Takes an argument for a test hemoglobin and glucose and a data hemoglobin and 
	glucose. It uses these values to calculate distance. It returns the distance. 

-Scaled
	-Takes glucose and hemoglobin arrays as arguments. Scales/normalizesS glucose and 	hemoglobin. Returns the scaled glucose and scaled hemoglobin.

-AssignToCentroid
	-This function has no parameters. It assigns each data point in ckd to its 
    	closest Centroid. It returns a list of each assignment.

-UpdateCentroids
	- This function has a parameter K, the number of centroids. It uses the list of 	assigned centroids to find an average location and updates the centroid to this 	average location. It returns a list of the updated centroids.

-graphingKMeans
	-This function takes parameters glucose, hemoglobin, assignment, and centroids. It 	plots the glucose and centroids with the color of their assigned centroid. It 		plots the centroid. It has no return value.

-Calculate_Accuracy
	-This function, if K == 2, calculates true and false positives and negatives. 
    	It prints a label and the percentages of each. It has no return value.
