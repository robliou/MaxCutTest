import neal
import numpy as np
import time

import matplotlib.pyplot as plt

import sys
sys.path.append("./../data")

import convert_to_matrix_500_30 
# 100 x 100 example matrix
#matrix = np.random.rand(100, 100)



matrix_raw = np.zeros((500, 500))
# Loop through the list of tuples and set corresponding positions to 1
for pos in convert_to_matrix_500_30.lst:
    row = pos[0]
    col = pos[1]
    val = pos[2]
    matrix_raw[row][col] = val

# Print the matrix
print(matrix_raw)

matrix = -np.array(matrix_raw)

def num_cut_edges(initial_matrix, ground_state_solution):
    num_edges = 0
    for i in range(len(initial_matrix)):
        for j in range(i+1, len(initial_matrix)):
            if initial_matrix[i][j] == 1 and ground_state_solution[i]*ground_state_solution[j] == -1:
                num_edges += 1
    return num_edges



# convert matrix to max-cut problem
h = {}
J = {}
for i in range(500):
    for j in range(i+1, 500):
        if matrix[i][j] < 0.0:
            J[(i, j)] = 1.0
        #else:
          #  J[(i, j)] = -1.0



#print('this is h', h)
#print('this is J', J)

#print('this is matrix[1][5]', matrix[1][5])

# Create an empty array
my_array = []






final_time=0

for i in range(100):
    start_time = time.perf_counter()


    # solve problem using simulated annealing
    sampler = neal.SimulatedAnnealingSampler()
    sampleset = sampler.sample_ising(h, J, num_reads=40)
    num_edges = num_cut_edges(matrix_raw, sampleset.first.sample)
    final_time = time.perf_counter() - start_time 

    my_array.append((num_edges, final_time))


my_array = np.array(my_array)

# Save the array as a NumPy array locally
np.save('my_array.npy', my_array)


# Save the array as a text file
np.savetxt('my_array.txt', my_array) 

print("my_array ", my_array)


print("Number of cut edges: ", num_edges)


# Extract the x and y coordinates from the array of tuples
x = my_array[:, 0]
y = my_array[:, 1]

# Plot the points
plt.scatter(x, y)
plt.xlabel('# cuts ')
plt.ylabel('time in seconds')

# Calculate the average of the y-coordinates
average_x = np.mean(x)

average_y = np.mean(y)

# Print the average of the y-coordinates
print("The average of the x-axis values is:", average_x)

# Print the average of the y-coordinates
print("The average of the y-axis values is:", average_y)


# print energy of first solution
print(sampleset.first.energy)


# Show the plot
plt.show()