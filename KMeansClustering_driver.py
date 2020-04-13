#Please place your FUNCTION (I assume the driver holds main code, not functions) for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions

K = 2
Centroids = np.random.rand(K,2)
glucose, hemoglobin, classification = openckdfile()
glucose_scaled, hemoglobin_scaled = Scaled(glucose, hemoglobin)
count = 0
Updated_Centroids = np.array(UpdateCentroids(K))
Assignment_Array = np.array(AssignToCentroid())

while True:
        count += 1
        Assignment_Array = np.array(AssignToCentroid())
        graphingKMeans(glucose_scaled, hemoglobin_scaled, Assignment_Array, Centroids)
        Centroids = UpdateCentroids(K)
        if Centroids[0][0] == np.array(UpdateCentroids(K))[0][0]:
            break
        if count == 25:
            break

Calculate_Accuracy(K)