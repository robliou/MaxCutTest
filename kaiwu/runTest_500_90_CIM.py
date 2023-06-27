# 导入 numpy 与 kaiwu
import numpy as np
import kaiwu as kw

# 导入绘图库
import matplotlib.pyplot as plt
import sys
sys.path.append("./../data")

import convert_to_matrix_500_90

import time
start_time = time.perf_counter()

matrix_reformed = np.zeros((500, 500))
# Loop through the list of tuples and set corresponding positions to 1
for pos in convert_to_matrix_500_90.lst:
    row = pos[0]
    col = pos[1]
    val = pos[2]
    matrix_reformed[row][col] = val

print('this is matrix_reformed', matrix_reformed)




matrix = -np.array(matrix_reformed)

# Print the matrix
print('this is matrix', matrix)



def num_cut_edges(initial_matrix, ground_state_solution):
    num_edges = 0
    for i in range(len(initial_matrix)):
        for j in range(i+1, len(initial_matrix)):
            if initial_matrix[i][j] == 1 and ground_state_solution[i]*ground_state_solution[j] == -1:
                num_edges += 1
    return num_edges


#plt.figure(figsize=(10, 10))

# 绘制脉冲图
#plt.subplot(211)
#plt.plot(output, linewidth=1)
#plt.title("Pulse Phase")
#plt.ylabel("Phase")
#plt.xlabel("T")

# 绘制能量图
#plt.subplot(212)
#plt.plot(h, linewidth=1)
#plt.title("Hamiltonian")
#plt.ylabel("H")
#plt.xlabel("T")

#plt.show()




# Create an empty array
my_array = []


final_time=0

for i in range(100):
    start_time = time.perf_counter()

    matrix_n = kw.cim.normalizer(matrix, normalization=0.5)
    output = kw.cim.simulator_core(
            matrix_n,
            c = 0,
            pump = 0.7,
            noise = 0.01,
            laps = 1000,
            dt = 0.1)

    h = kw.sampler.hamiltonian(matrix, output)
    c_set = kw.sampler.binarizer(output)

    opt = kw.sampler.optimal_sampler(matrix, c_set, 0)

    best = opt[0][0]

    num_edges = num_cut_edges(matrix_reformed, best)
    final_time = time.perf_counter() - start_time 

    my_array.append((num_edges, final_time))


my_array = np.array(my_array)



# Save the array as a NumPy array locally
np.save('my_array.npy', my_array)


# Save the array as a text file
np.savetxt('my_array.txt', my_array) 

print("my_array ", my_array)


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


# Show the plot
plt.show()


print(best)
print("--- %s seconds ---" % (time.perf_counter() - start_time))

num_edges = num_cut_edges(matrix_reformed, best)

print("Number of cut edges1: ", num_edges)

arr = best
bitarray = [(i + 1) // 2 for i in arr]
print('this is bitarray', bitarray)
bitstring = ''.join(str(i) for i in bitarray)
print('this is bitString', bitstring)
