# Title: CSCE 311 - HW 5: Djikstra's Algorithm
# Author: Devin Boyle <dboyle@alaska.edu<
# Created: 4/14/2018

from collections import defaultdict

import numpy as np
import sys
import os


class GraphMatrix:

    # Print the shortest path from a point to a destination
    def print_path(self, parent_array, destination, path):

        if parent_array[destination] == -1:
            path.append(destination)
            return
        self.print_path(parent_array, parent_array[destination], path),
        path.append(destination)

    # Print the shortest path from a given start point, return the
    # final distance
    def get_shortest_paths(self, distance, parent_array, start, end):

        path = []
        self.print_path(parent_array, end, path)
        return path, distance[end]

    def find_index_of_minimum(self, distance, queue):

        minimum = float('inf')
        index_of_minimum = -1

        for i in range(len(distance)):
            if (distance[i] < minimum and i in queue):
                minimum = distance[i]
                index_of_minimum = i

        return index_of_minimum

    def djikstra_algorithm(self, graph_matrix, start, end):

        row = len(graph_matrix)
        column = len(graph_matrix[0])

        # Initialize all distances to maximum value
        distance = [float('inf')] * row

        # Initialize array that will hold shortest path
        parent_array = [-1] * row

        # Initial vertex has no distance from itself
        distance[start] = 0

        # Append all vertices to queue
        queue = []
        for i in range(row):
            queue.append(i)

        # Find the shortest path to all vertices

        # While there are values in the queue
        while queue:

            # Find enqueued vertex with minimum distance
            neighbor = self.find_index_of_minimum(distance, queue)

            # Remove minimum distance vertex from queue
            queue.remove(neighbor)

            # Update the distance value and the index of the shortest path
            for i in range(column):
                if graph_matrix[neighbor][i] and i in queue:
                    if distance[neighbor] \
                            + graph_matrix[neighbor][i] < distance[i]:
                        distance[i] = distance[neighbor]\
                                      + graph_matrix[neighbor][i]
                        parent_array[i] = neighbor
        return self.get_shortest_paths(distance, parent_array, start, end)

# Take in the filename argument
file_name = sys.argv[1]

flag = True
graph_representation = []

# Error checking for input file
while flag:
    flag = False
    graph_representation = []

    # If the file doesn't exist, print output and throw a flag
    if(not os.path.exists(file_name)):
        print("The file you entered was not found\n")
        flag = True
    else:
        with open(file_name) as f:
            for line in f:
                data = line.strip().split(",")
                int_data = []
                for item in data:
                    try:
                        int_data.append(int(item))
                    # If the input file is improperly formatted, print an
                    # error message and throw a flag
                    except ValueError as e:
                        print("A character in your graph representation was"
                              " not a number\n")
                        flag = True
                graph_representation.append(int_data)
    if not flag:
        matrix = np.array(graph_representation)
        # If the matrix was not symmetric, print and error message and
        # throw a flag.
        if(not np.array_equal(matrix.transpose(), matrix)):
            print("Your matrix was not symmetric.")
            flag = True
    if flag:
        file_name = input("Please check to make sure that your file is setup"
                          " correctly, or enter another filename: ")


graph_solver = GraphMatrix()

# Default location names
graph_names = ["Russian Embassy", "Reflecting Pool", "Train Station",
               "Cache 1", "Arboretum", "Lincoln Memorial", "Ford Theater",
               "Airport", "Cache 2", "Jefferson Memorial"]

# Default output values
paths = ["to Cache1 to Train Station",
         "to Cache1 to Airport",
         "to Cache2 to Train Station",
         "to Cache2 to Airport"
         ]

for i in graph_names:
    print("Starting point: ", i)
    paths_required = [[(graph_names.index(i), 3), (3, 2)],
                      [(graph_names.index(i), 3), (3, 7)],
                      [(graph_names.index(i), 8), (8, 2)],
                      [(graph_names.index(i), 8), (8, 7)]]

    for j in range(len(paths_required)):
        # Print the starting point, the second point, and the exit point
        print("From " + i + " to " + paths[j])
        a = paths_required[j][0][0]
        b = paths_required[j][0][1]
        c = paths_required[j][1][1]

        # Use Djikstra's algorithm to solve the shortest path from point
        # a to b, then from point b to c
        path = []
        p1, d1 = graph_solver.djikstra_algorithm(graph_representation, a, b)
        p2, d2 = graph_solver.djikstra_algorithm(graph_representation, b, c)

        path = p1 + p2[1:]
        for p in path[:-1]:
            print(graph_names[p] + ", ", end="")
        print(graph_names[path[-1]])
        # Print the overall time of the route by combining the
        # distances of each Djikstra call
        print("Estimated Time: " + str(d1 + d2) + " minutes.")
        print()

    print('-----------------------------------------------------------------')
