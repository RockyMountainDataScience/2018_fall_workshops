
# Set up libraries
# -- Numpy --
import numpy as np
from numpy.random import normal
from numpy.linalg import norm
from numpy.random import binomial
# -- Graphing --
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# K_MEANS function
#   Input: data - an array of data points
#          number_of_clusters - integer storing number of clusters used in k-means
#          iterations - integer storing number of times to run algorithm
#   Output: cluster_labels - an array stating which cluster each data point belongs to
#           cluster_centers - an array with the data point at the center of each cluster
def k_means(data, number_of_clusters, iterations):

    # Randomly assign points to a cluster center for an initial guess
    cluster_labels = np.random.randint(0, number_of_clusters, size=len(data[0]))
    # Generate a vector of cluster centers of the shape we need
    cluster_centers = np.zeros((number_of_clusters, 2))
    # Create a for loop to operate a specific number of iterations
    for _ in range(iterations):

        # Perform the first step of K-means -- Update Step
        # Compute the mean of each of the points within a specific cluster

        for cluster_center_index in range(number_of_clusters):
            working_data_index = 0
            for in_cluster_index in cluster_center_index == cluster_labels:
                if(in_cluster_index and working_data_index <= len(data[0])):
                    working_data = [data[0][working_data_index], data[1][working_data_index]]
                    cluster_centers[cluster_center_index] = np.mean(working_data, axis=0)
                    working_data_index += 1

        # Perform the second step of K-means -- Assignment Step
        # Assign each point to the nearest cluster center

        # Save the index to the cluster center list
        best_so_far_index = number_of_clusters

        for data_point_index in range(len(data[0])):

            # Save best_so_far as the minimum distance seen for that data point
            # to each of the cluster centers
            best_so_far = 1000000000

            # Check all cluster centers and update best_so_far and best_so_far_index only if
            # better value is observed
            for cluster_center_index in range(number_of_clusters):
                working_data = [data[0][data_point_index], data[1][data_point_index]]
                if norm(cluster_centers[cluster_center_index] - working_data) < best_so_far:
                    best_so_far = norm(cluster_centers[cluster_center_index] - working_data)
                    best_so_far_index = cluster_center_index

            # Assign the best_so_far_index to the associated cluster_center index
            cluster_labels[data_point_index] = best_so_far_index

        ## TODO: Debug K-means via scatterplot


    # return both cluster labels (which cluster data points belong to) and
    # cluster centers (the centers of those clusters)

    return cluster_labels, cluster_centers

# # TODO: link file to data set or simulate a data set in the variable dataset
#         where dataset[0] is the x-coords of the data and dataset[1] is the
#         dataset[1] is the y-coords of the data


## TODO: Fill in function call with last two input items
labels, centers = k_means( dataset, , )
sns.scatterplot(x = dataset[0], y = dataset[1], hue=labels)
plt.show()
