import neal
import numpy as np
import time
import matplotlib.pyplot as plt

# 100 x 100 example matrix
#matrix = np.random.rand(100, 100)

lst = [[0, 5, 1], [0, 9, 1], [0, 11, 1], [0, 17, 1], [0, 18, 1], [0, 21, 1], [0, 22, 1], [0, 30, 1], [0, 31, 1], [0, 32, 1], [0, 36, 1], [0, 37, 1], [0, 42, 1], [0, 44, 1], [0, 47, 1], [0, 51, 1], [0, 52, 1], [0, 53, 1], [0, 54, 1], [0, 55, 1], [0, 59, 1], [0, 61, 1], [0, 62, 1], [0, 67, 1], [0, 69, 1], [0, 70, 1], [0, 74, 1], [0, 83, 1], [0, 86, 1], [0, 88, 1], [0, 92, 1], [0, 95, 1], [0, 96, 1], [0, 98, 1], [1, 2, 1], [1, 6, 1], [1, 12, 1], [1, 13, 1], [1, 16, 1], [1, 18, 1], [1, 19, 1], [1, 21, 1], [1, 27, 1], [1, 30, 1], [1, 31, 1], [1, 32, 1], [1, 34, 1], [1, 42, 1], [1, 43, 1], [1, 47, 1], [1, 48, 1], [1, 52, 1], [1, 59, 1], [1, 62, 1], [1, 68, 1], [1, 69, 1], [1, 77, 1], [1, 81, 1], [1, 83, 1], [1, 85, 1], [1, 86, 1], [1, 92, 1], [1, 99, 1], [2, 1, 1], [2, 3, 1], [2, 4, 1], [2, 13, 1], [2, 20, 1], [2, 36, 1], [2, 39, 1], [2, 40, 1], [2, 42, 1], [2, 44, 1], [2, 49, 1], [2, 50, 1], [2, 51, 1], [2, 53, 1], [2, 54, 1], [2, 66, 1], [2, 67, 1], [2, 69, 1], [2, 74, 1], [2, 76, 1], [2, 78, 1], [2, 79, 1], [2, 82, 1], [2, 83, 1], [2, 87, 1], [2, 92, 1], [2, 94, 1], [2, 95, 1], [3, 2, 1], [3, 4, 1], [3, 6, 1], [3, 9, 1], [3, 10, 1], [3, 11, 1], [3, 12, 1], [3, 13, 1], [3, 15, 1], [3, 16, 1], [3, 19, 1], [3, 22, 1], [3, 24, 1], [3, 25, 1], [3, 28, 1], [3, 31, 1], [3, 32, 1], [3, 34, 1], [3, 35, 1], [3, 36, 1], [3, 41, 1], [3, 48, 1], [3, 50, 1], [3, 54, 1], [3, 55, 1], [3, 60, 1], [3, 65, 1], [3, 66, 1], [3, 74, 1], [3, 77, 1], [3, 82, 1], [3, 83, 1], [3, 84, 1], [3, 86, 1], [3, 87, 1], [3, 90, 1], [3, 93, 1], [3, 96, 1], [3, 97, 1], [4, 2, 1], [4, 3, 1], [4, 8, 1], [4, 9, 1], [4, 11, 1], [4, 13, 1], [4, 20, 1], [4, 21, 1], [4, 25, 1], [4, 26, 1], [4, 27, 1], [4, 34, 1], [4, 35, 1], [4, 37, 1], [4, 39, 1], [4, 41, 1], [4, 45, 1], [4, 48, 1], [4, 49, 1], [4, 51, 1], [4, 55, 1], [4, 56, 1], [4, 59, 1], [4, 66, 1], [4, 70, 1], [4, 71, 1], [4, 73, 1], [4, 74, 1], [4, 76, 1], [4, 77, 1], [4, 82, 1], [4, 90, 1], [4, 94, 1], [4, 96, 1], [4, 97, 1], [4, 98, 1], [4, 99, 1], [5, 0, 1], [5, 13, 1], [5, 22, 1], [5, 25, 1], [5, 29, 1], [5, 30, 1], [5, 31, 1], [5, 33, 1], [5, 40, 1], [5, 41, 1], [5, 42, 1], [5, 48, 1], [5, 49, 1], [5, 53, 1], [5, 54, 1], [5, 65, 1], [5, 67, 1], [5, 68, 1], [5, 69, 1], [5, 76, 1], [5, 80, 1], [5, 81, 1], [5, 86, 1], [5, 88, 1], [5, 90, 1], [5, 95, 1], [5, 96, 1], [6, 1, 1], [6, 3, 1], [6, 8, 1], [6, 9, 1], [6, 10, 1], [6, 14, 1], [6, 15, 1], [6, 20, 1], [6, 29, 1], [6, 30, 1], [6, 33, 1], [6, 36, 1], [6, 40, 1], [6, 41, 1], [6, 42, 1], [6, 43, 1], [6, 50, 1], [6, 53, 1], [6, 54, 1], [6, 59, 1], [6, 60, 1], [6, 62, 1], [6, 66, 1], [6, 73, 1], [6, 77, 1], [6, 80, 1], [6, 81, 1], [6, 82, 1], [6, 86, 1], [6, 88, 1], [6, 89, 1], [6, 91, 1], [6, 92, 1], [6, 93, 1], [6, 95, 1], [6, 97, 1], [6, 98, 1], [7, 10, 1], [7, 15, 1], [7, 16, 1], [7, 34, 1], [7, 35, 1], [7, 38, 1], [7, 44, 1], [7, 46, 1], [7, 50, 1], [7, 51, 1], [7, 52, 1], [7, 57, 1], [7, 64, 1], [7, 65, 1], [7, 66, 1], [7, 79, 1], [7, 80, 1], [7, 82, 1], [7, 83, 1], [7, 85, 1], [7, 90, 1], [7, 93, 1], [7, 98, 1], [8, 4, 1], [8, 6, 1], [8, 13, 1], [8, 14, 1], [8, 15, 1], [8, 19, 1], [8, 21, 1], [8, 22, 1], [8, 28, 1], [8, 30, 1], [8, 33, 1], [8, 37, 1], [8, 38, 1], [8, 40, 1], [8, 41, 1], [8, 50, 1], [8, 51, 1], [8, 52, 1], [8, 56, 1], [8, 60, 1], [8, 63, 1], [8, 64, 1], [8, 66, 1], [8, 68, 1], [8, 69, 1], [8, 74, 1], [8, 77, 1], [8, 82, 1], [8, 85, 1], [8, 88, 1], [8, 91, 1], [8, 92, 1], [8, 93, 1], [8, 95, 1], [9, 0, 1], [9, 3, 1], [9, 4, 1], [9, 6, 1], [9, 11, 1], [9, 20, 1], [9, 33, 1], [9, 36, 1], [9, 40, 1], [9, 41, 1], [9, 45, 1], [9, 46, 1], [9, 49, 1], [9, 61, 1], [9, 63, 1], [9, 65, 1], [9, 68, 1], [9, 74, 1], [9, 82, 1], [9, 84, 1], [9, 87, 1], [9, 88, 1], [9, 90, 1], [9, 98, 1], [9, 99, 1], [10, 3, 1], [10, 6, 1], [10, 7, 1], [10, 12, 1], [10, 13, 1], [10, 14, 1], [10, 18, 1], [10, 25, 1], [10, 31, 1], [10, 35, 1], [10, 53, 1], [10, 58, 1], [10, 62, 1], [10, 69, 1], [10, 71, 1], [10, 74, 1], [10, 80, 1], [10, 84, 1], [10, 86, 1], [10, 89, 1], [10, 93, 1], [10, 94, 1], [11, 0, 1], [11, 3, 1], [11, 4, 1], [11, 9, 1], [11, 12, 1], [11, 17, 1], [11, 18, 1], [11, 21, 1], [11, 23, 1], [11, 24, 1], [11, 26, 1], [11, 29, 1], [11, 32, 1], [11, 33, 1], [11, 39, 1], [11, 43, 1], [11, 47, 1], [11, 48, 1], [11, 50, 1], [11, 51, 1], [11, 54, 1], [11, 56, 1], [11, 57, 1], [11, 64, 1], [11, 66, 1], [11, 69, 1], [11, 74, 1], [11, 77, 1], [11, 81, 1], [11, 82, 1], [11, 91, 1], [11, 94, 1], [11, 96, 1], [12, 1, 1], [12, 3, 1], [12, 10, 1], [12, 11, 1], [12, 18, 1], [12, 23, 1], [12, 25, 1], [12, 27, 1], [12, 28, 1], [12, 30, 1], [12, 31, 1], [12, 39, 1], [12, 41, 1], [12, 44, 1], [12, 46, 1], [12, 47, 1], [12, 48, 1], [12, 54, 1], [12, 57, 1], [12, 60, 1], [12, 62, 1], [12, 65, 1], [12, 66, 1], [12, 75, 1], [12, 77, 1], [12, 85, 1], [12, 97, 1], [12, 98, 1], [13, 1, 1], [13, 2, 1], [13, 3, 1], [13, 4, 1], [13, 5, 1], [13, 8, 1], [13, 10, 1], [13, 17, 1], [13, 19, 1], [13, 20, 1], [13, 27, 1], [13, 29, 1], [13, 30, 1], [13, 31, 1], [13, 32, 1], [13, 33, 1], [13, 35, 1], [13, 37, 1], [13, 39, 1], [13, 41, 1], [13, 42, 1], [13, 47, 1], [13, 48, 1], [13, 53, 1], [13, 55, 1], [13, 58, 1], [13, 63, 1], [13, 64, 1], [13, 71, 1], [13, 78, 1], [13, 79, 1], [13, 80, 1], [13, 87, 1], [13, 95, 1], [13, 96, 1], [14, 6, 1], [14, 8, 1], [14, 10, 1], [14, 16, 1], [14, 17, 1], [14, 19, 1], [14, 20, 1], [14, 21, 1], [14, 36, 1], [14, 38, 1], [14, 41, 1], [14, 45, 1], [14, 49, 1], [14, 52, 1], [14, 54, 1], [14, 57, 1], [14, 62, 1], [14, 63, 1], [14, 64, 1], [14, 70, 1], [14, 74, 1], [14, 75, 1], [14, 77, 1], [14, 80, 1], [14, 81, 1], [14, 82, 1], [14, 84, 1], [14, 86, 1], [14, 97, 1], [14, 99, 1], [15, 3, 1], [15, 6, 1], [15, 7, 1], [15, 8, 1], [15, 16, 1], [15, 20, 1], [15, 22, 1], [15, 29, 1], [15, 30, 1], [15, 35, 1], [15, 41, 1], [15, 42, 1], [15, 45, 1], [15, 49, 1], [15, 57, 1], [15, 58, 1], [15, 60, 1], [15, 67, 1], [15, 70, 1], [15, 73, 1], [15, 76, 1], [15, 86, 1], [15, 88, 1], [15, 91, 1], [15, 93, 1], [15, 97, 1], [15, 98, 1], [15, 99, 1], [16, 1, 1], [16, 3, 1], [16, 7, 1], [16, 14, 1], [16, 15, 1], [16, 26, 1], [16, 27, 1], [16, 28, 1], [16, 29, 1], [16, 33, 1], [16, 34, 1], [16, 36, 1], [16, 37, 1], [16, 42, 1], [16, 44, 1], [16, 45, 1], [16, 53, 1], [16, 55, 1], [16, 60, 1], [16, 64, 1], [16, 69, 1], [16, 74, 1], [16, 77, 1], [16, 78, 1], [16, 83, 1], [16, 84, 1], [16, 89, 1], [16, 92, 1], [16, 94, 1], [16, 95, 1], [16, 96, 1], [16, 97, 1], [16, 99, 1], [17, 0, 1], [17, 11, 1], [17, 13, 1], [17, 14, 1], [17, 18, 1], [17, 24, 1], [17, 25, 1], [17, 27, 1], [17, 29, 1], [17, 36, 1], [17, 37, 1], [17, 40, 1], [17, 41, 1], [17, 47, 1], [17, 54, 1], [17, 55, 1], [17, 66, 1], [17, 69, 1], [17, 71, 1], [17, 72, 1], [17, 77, 1], [17, 78, 1], [17, 79, 1], [17, 82, 1], [17, 85, 1], [17, 88, 1], [17, 91, 1], [17, 92, 1], [17, 93, 1], [17, 94, 1], [17, 98, 1], [18, 0, 1], [18, 1, 1], [18, 10, 1], [18, 11, 1], [18, 12, 1], [18, 17, 1], [18, 26, 1], [18, 27, 1], [18, 29, 1], [18, 34, 1], [18, 37, 1], [18, 38, 1], [18, 40, 1], [18, 41, 1], [18, 42, 1], [18, 43, 1], [18, 45, 1], [18, 47, 1], [18, 48, 1], [18, 51, 1], [18, 53, 1], [18, 54, 1], [18, 59, 1], [18, 62, 1], [18, 63, 1], [18, 64, 1], [18, 65, 1], [18, 67, 1], [18, 69, 1], [18, 71, 1], [18, 75, 1], [18, 76, 1], [18, 77, 1], [18, 80, 1], [18, 82, 1], [18, 85, 1], [18, 88, 1], [18, 89, 1], [18, 90, 1], [18, 91, 1], [18, 93, 1], [18, 97, 1], [18, 98, 1], [19, 1, 1], [19, 3, 1], [19, 8, 1], [19, 13, 1], [19, 14, 1], [19, 23, 1], [19, 24, 1], [19, 32, 1], [19, 35, 1], [19, 36, 1], [19, 39, 1], [19, 41, 1], [19, 42, 1], [19, 44, 1], [19, 45, 1], [19, 46, 1], [19, 56, 1], [19, 60, 1], [19, 64, 1], [19, 67, 1], [19, 68, 1], [19, 70, 1], [19, 71, 1], [19, 72, 1], [19, 74, 1], [19, 75, 1], [19, 79, 1], [19, 83, 1], [19, 89, 1], [19, 93, 1], [19, 94, 1], [19, 95, 1], [19, 97, 1], [19, 99, 1], [20, 2, 1], [20, 4, 1], [20, 6, 1], [20, 9, 1], [20, 13, 1], [20, 14, 1], [20, 15, 1], [20, 32, 1], [20, 42, 1], [20, 44, 1], [20, 49, 1], [20, 58, 1], [20, 64, 1], [20, 67, 1], [20, 68, 1], [20, 69, 1], [20, 75, 1], [20, 76, 1], [20, 81, 1], [20, 83, 1], [20, 85, 1], [20, 90, 1], [20, 93, 1], [20, 94, 1], [20, 98, 1], [21, 0, 1], [21, 1, 1], [21, 4, 1], [21, 8, 1], [21, 11, 1], [21, 14, 1], [21, 28, 1], [21, 33, 1], [21, 34, 1], [21, 38, 1], [21, 40, 1], [21, 42, 1], [21, 43, 1], [21, 44, 1], [21, 54, 1], [21, 60, 1], [21, 61, 1], [21, 69, 1], [21, 72, 1], [21, 80, 1], [21, 81, 1], [21, 83, 1], [21, 86, 1], [21, 92, 1], [21, 96, 1], [21, 98, 1], [21, 99, 1], [22, 0, 1], [22, 3, 1], [22, 5, 1], [22, 8, 1], [22, 15, 1], [22, 24, 1], [22, 30, 1], [22, 31, 1], [22, 33, 1], [22, 35, 1], [22, 38, 1], [22, 47, 1], [22, 52, 1], [22, 53, 1], [22, 55, 1], [22, 64, 1], [22, 67, 1], [22, 68, 1], [22, 69, 1], [22, 72, 1], [22, 74, 1], [22, 75, 1], [22, 76, 1], [22, 81, 1], [22, 83, 1], [22, 89, 1], [22, 95, 1], [22, 98, 1], [22, 99, 1], [23, 11, 1], [23, 12, 1], [23, 19, 1], [23, 24, 1], [23, 26, 1], [23, 28, 1], [23, 37, 1], [23, 41, 1], [23, 44, 1], [23, 48, 1], [23, 49, 1], [23, 55, 1], [23, 66, 1], [23, 68, 1], [23, 69, 1], [23, 70, 1], [23, 73, 1], [23, 75, 1], [23, 76, 1], [23, 81, 1], [23, 82, 1], [23, 85, 1], [23, 89, 1], [23, 92, 1], [23, 93, 1], [24, 3, 1], [24, 11, 1], [24, 17, 1], [24, 19, 1], [24, 22, 1], [24, 23, 1], [24, 26, 1], [24, 27, 1], [24, 36, 1], [24, 40, 1], [24, 42, 1], [24, 43, 1], [24, 45, 1], [24, 48, 1], [24, 53, 1], [24, 58, 1], [24, 59, 1], [24, 63, 1], [24, 66, 1], [24, 77, 1], [24, 85, 1], [24, 87, 1], [24, 92, 1], [24, 97, 1], [24, 99, 1], [25, 3, 1], [25, 4, 1], [25, 5, 1], [25, 10, 1], [25, 12, 1], [25, 17, 1], [25, 28, 1], [25, 31, 1], [25, 34, 1], [25, 36, 1], [25, 47, 1], [25, 50, 1], [25, 58, 1], [25, 60, 1], [25, 62, 1], [25, 63, 1], [25, 64, 1], [25, 72, 1], [25, 73, 1], [25, 78, 1], [25, 85, 1], [25, 88, 1], [25, 91, 1], [25, 92, 1], [26, 4, 1], [26, 11, 1], [26, 16, 1], [26, 18, 1], [26, 23, 1], [26, 24, 1], [26, 31, 1], [26, 39, 1], [26, 43, 1], [26, 44, 1], [26, 50, 1], [26, 51, 1], [26, 52, 1], [26, 56, 1], [26, 60, 1], [26, 65, 1], [26, 66, 1], [26, 69, 1], [26, 71, 1], [26, 74, 1], [26, 76, 1], [26, 84, 1], [26, 89, 1], [26, 90, 1], [26, 91, 1], [26, 96, 1], [26, 98, 1], [27, 1, 1], [27, 4, 1], [27, 12, 1], [27, 13, 1], [27, 16, 1], [27, 17, 1], [27, 18, 1], [27, 24, 1], [27, 30, 1], [27, 32, 1], [27, 35, 1], [27, 40, 1], [27, 41, 1], [27, 42, 1], [27, 43, 1], [27, 45, 1], [27, 49, 1], [27, 56, 1], [27, 59, 1], [27, 63, 1], [27, 64, 1], [27, 65, 1], [27, 72, 1], [27, 77, 1], [27, 83, 1], [27, 95, 1], [27, 96, 1], [27, 97, 1], [27, 98, 1], [28, 3, 1], [28, 8, 1], [28, 12, 1], [28, 16, 1], [28, 21, 1], [28, 23, 1], [28, 25, 1], [28, 29, 1], [28, 31, 1], [28, 33, 1], [28, 34, 1], [28, 36, 1], [28, 37, 1], [28, 39, 1], [28, 40, 1], [28, 42, 1], [28, 47, 1], [28, 54, 1], [28, 60, 1], [28, 61, 1], [28, 63, 1], [28, 66, 1], [28, 68, 1], [28, 70, 1], [28, 72, 1], [28, 76, 1], [28, 80, 1], [28, 82, 1], [28, 85, 1], [28, 88, 1], [28, 89, 1], [28, 95, 1], [28, 98, 1], [29, 5, 1], [29, 6, 1], [29, 11, 1], [29, 13, 1], [29, 15, 1], [29, 16, 1], [29, 17, 1], [29, 18, 1], [29, 28, 1], [29, 32, 1], [29, 35, 1], [29, 42, 1], [29, 50, 1], [29, 53, 1], [29, 55, 1], [29, 56, 1], [29, 58, 1], [29, 60, 1], [29, 71, 1], [29, 84, 1], [29, 85, 1], [29, 86, 1], [29, 94, 1], [29, 97, 1], [30, 0, 1], [30, 1, 1], [30, 5, 1], [30, 6, 1], [30, 8, 1], [30, 12, 1], [30, 13, 1], [30, 15, 1], [30, 22, 1], [30, 27, 1], [30, 31, 1], [30, 39, 1], [30, 41, 1], [30, 45, 1], [30, 46, 1], [30, 59, 1], [30, 63, 1], [30, 64, 1], [30, 65, 1], [30, 71, 1], [30, 80, 1], [30, 84, 1], [30, 91, 1], [30, 94, 1], [30, 96, 1], [31, 0, 1], [31, 1, 1], [31, 3, 1], [31, 5, 1], [31, 10, 1], [31, 12, 1], [31, 13, 1], [31, 22, 1], [31, 25, 1], [31, 26, 1], [31, 28, 1], [31, 30, 1], [31, 33, 1], [31, 42, 1], [31, 46, 1], [31, 47, 1], [31, 53, 1], [31, 55, 1], [31, 75, 1], [31, 80, 1], [31, 81, 1], [31, 87, 1], [31, 88, 1], [31, 89, 1], [31, 96, 1], [31, 99, 1], [32, 0, 1], [32, 1, 1], [32, 3, 1], [32, 11, 1], [32, 13, 1], [32, 19, 1], [32, 20, 1], [32, 27, 1], [32, 29, 1], [32, 35, 1], [32, 41, 1], [32, 44, 1], [32, 50, 1], [32, 52, 1], [32, 60, 1], [32, 61, 1], [32, 67, 1], [32, 70, 1], [32, 74, 1], [32, 75, 1], [32, 81, 1], [32, 82, 1], [32, 84, 1], [32, 91, 1], [32, 92, 1], [32, 94, 1], [32, 96, 1], [32, 99, 1], [33, 5, 1], [33, 6, 1], [33, 8, 1], [33, 9, 1], [33, 11, 1], [33, 13, 1], [33, 16, 1], [33, 21, 1], [33, 22, 1], [33, 28, 1], [33, 31, 1], [33, 34, 1], [33, 35, 1], [33, 36, 1], [33, 38, 1], [33, 41, 1], [33, 42, 1], [33, 44, 1], [33, 45, 1], [33, 46, 1], [33, 47, 1], [33, 48, 1], [33, 49, 1], [33, 53, 1], [33, 55, 1], [33, 57, 1], [33, 59, 1], [33, 64, 1], [33, 66, 1], [33, 67, 1], [33, 75, 1], [33, 76, 1], [33, 78, 1], [33, 79, 1], [33, 81, 1], [33, 87, 1], [33, 89, 1], [33, 90, 1], [33, 91, 1], [33, 92, 1], [33, 96, 1], [33, 97, 1], [34, 1, 1], [34, 3, 1], [34, 4, 1], [34, 7, 1], [34, 16, 1], [34, 18, 1], [34, 21, 1], [34, 25, 1], [34, 28, 1], [34, 33, 1], [34, 35, 1], [34, 38, 1], [34, 40, 1], [34, 42, 1], [34, 43, 1], [34, 45, 1], [34, 47, 1], [34, 49, 1], [34, 53, 1], [34, 57, 1], [34, 58, 1], [34, 65, 1], [34, 68, 1], [34, 71, 1], [34, 72, 1], [34, 74, 1], [34, 78, 1], [34, 82, 1], [34, 86, 1], [34, 97, 1], [34, 98, 1], [35, 3, 1], [35, 4, 1], [35, 7, 1], [35, 10, 1], [35, 13, 1], [35, 15, 1], [35, 19, 1], [35, 22, 1], [35, 27, 1], [35, 29, 1], [35, 32, 1], [35, 33, 1], [35, 34, 1], [35, 36, 1], [35, 38, 1], [35, 41, 1], [35, 43, 1], [35, 44, 1], [35, 45, 1], [35, 46, 1], [35, 51, 1], [35, 60, 1], [35, 64, 1], [35, 65, 1], [35, 66, 1], [35, 67, 1], [35, 75, 1], [35, 76, 1], [35, 77, 1], [35, 81, 1], [35, 84, 1], [35, 86, 1], [35, 91, 1], [35, 94, 1], [36, 0, 1], [36, 2, 1], [36, 3, 1], [36, 6, 1], [36, 9, 1], [36, 14, 1], [36, 16, 1], [36, 17, 1], [36, 19, 1], [36, 24, 1], [36, 25, 1], [36, 28, 1], [36, 33, 1], [36, 35, 1], [36, 37, 1], [36, 40, 1], [36, 41, 1], [36, 42, 1], [36, 43, 1], [36, 44, 1], [36, 45, 1], [36, 50, 1], [36, 51, 1], [36, 54, 1], [36, 56, 1], [36, 57, 1], [36, 58, 1], [36, 59, 1], [36, 61, 1], [36, 66, 1], [36, 68, 1], [36, 77, 1], [36, 78, 1], [36, 79, 1], [36, 86, 1], [36, 87, 1], [36, 90, 1], [36, 92, 1], [36, 93, 1], [37, 0, 1], [37, 4, 1], [37, 8, 1], [37, 13, 1], [37, 16, 1], [37, 17, 1], [37, 18, 1], [37, 23, 1], [37, 28, 1], [37, 36, 1], [37, 38, 1], [37, 39, 1], [37, 41, 1], [37, 42, 1], [37, 47, 1], [37, 58, 1], [37, 60, 1], [37, 63, 1], [37, 64, 1], [37, 66, 1], [37, 74, 1], [37, 75, 1], [37, 76, 1], [37, 77, 1], [37, 79, 1], [37, 80, 1], [37, 81, 1], [37, 85, 1], [37, 86, 1], [37, 88, 1], [37, 90, 1], [37, 91, 1], [37, 92, 1], [37, 93, 1], [37, 94, 1], [37, 97, 1], [38, 7, 1], [38, 8, 1], [38, 14, 1], [38, 18, 1], [38, 21, 1], [38, 22, 1], [38, 33, 1], [38, 34, 1], [38, 35, 1], [38, 37, 1], [38, 44, 1], [38, 50, 1], [38, 55, 1], [38, 58, 1], [38, 66, 1], [38, 71, 1], [38, 73, 1], [38, 79, 1], [38, 80, 1], [38, 84, 1], [38, 86, 1], [38, 88, 1], [38, 92, 1], [38, 95, 1], [38, 96, 1], [38, 98, 1], [39, 2, 1], [39, 4, 1], [39, 11, 1], [39, 12, 1], [39, 13, 1], [39, 19, 1], [39, 26, 1], [39, 28, 1], [39, 30, 1], [39, 37, 1], [39, 41, 1], [39, 43, 1], [39, 46, 1], [39, 47, 1], [39, 48, 1], [39, 51, 1], [39, 60, 1], [39, 61, 1], [39, 63, 1], [39, 64, 1], [39, 71, 1], [39, 75, 1], [39, 76, 1], [39, 77, 1], [39, 78, 1], [39, 80, 1], [39, 81, 1], [39, 84, 1], [39, 87, 1], [39, 91, 1], [39, 93, 1], [39, 95, 1], [39, 98, 1], [40, 2, 1], [40, 5, 1], [40, 6, 1], [40, 8, 1], [40, 9, 1], [40, 17, 1], [40, 18, 1], [40, 21, 1], [40, 24, 1], [40, 27, 1], [40, 28, 1], [40, 34, 1], [40, 36, 1], [40, 43, 1], [40, 44, 1], [40, 45, 1], [40, 49, 1], [40, 55, 1], [40, 57, 1], [40, 60, 1], [40, 62, 1], [40, 67, 1], [40, 73, 1], [40, 75, 1], [40, 76, 1], [40, 82, 1], [40, 83, 1], [40, 86, 1], [40, 92, 1], [40, 98, 1], [41, 3, 1], [41, 4, 1], [41, 5, 1], [41, 6, 1], [41, 8, 1], [41, 9, 1], [41, 12, 1], [41, 13, 1], [41, 14, 1], [41, 15, 1], [41, 17, 1], [41, 18, 1], [41, 19, 1], [41, 23, 1], [41, 27, 1], [41, 30, 1], [41, 32, 1], [41, 33, 1], [41, 35, 1], [41, 36, 1], [41, 37, 1], [41, 39, 1], [41, 44, 1], [41, 46, 1], [41, 49, 1], [41, 50, 1], [41, 56, 1], [41, 63, 1], [41, 67, 1], [41, 68, 1], [41, 69, 1], [41, 72, 1], [41, 77, 1], [41, 81, 1], [41, 84, 1], [41, 85, 1], [41, 86, 1], [41, 87, 1], [41, 88, 1], [41, 96, 1], [42, 0, 1], [42, 1, 1], [42, 2, 1], [42, 5, 1], [42, 6, 1], [42, 13, 1], [42, 15, 1], [42, 16, 1], [42, 18, 1], [42, 19, 1], [42, 20, 1], [42, 21, 1], [42, 24, 1], [42, 27, 1], [42, 28, 1], [42, 29, 1], [42, 31, 1], [42, 33, 1], [42, 34, 1], [42, 36, 1], [42, 37, 1], [42, 45, 1], [42, 46, 1], [42, 49, 1], [42, 52, 1], [42, 54, 1], [42, 57, 1], [42, 61, 1], [42, 74, 1], [42, 78, 1], [42, 82, 1], [42, 83, 1], [42, 86, 1], [42, 89, 1], [42, 95, 1], [42, 97, 1], [43, 1, 1], [43, 6, 1], [43, 11, 1], [43, 18, 1], [43, 21, 1], [43, 24, 1], [43, 26, 1], [43, 27, 1], [43, 34, 1], [43, 35, 1], [43, 36, 1], [43, 39, 1], [43, 40, 1], [43, 47, 1], [43, 49, 1], [43, 52, 1], [43, 54, 1], [43, 58, 1], [43, 60, 1], [43, 62, 1], [43, 66, 1], [43, 73, 1], [43, 77, 1], [43, 80, 1], [43, 86, 1], [43, 89, 1], [43, 90, 1], [43, 93, 1], [43, 94, 1], [44, 0, 1], [44, 2, 1], [44, 7, 1], [44, 12, 1], [44, 16, 1], [44, 19, 1], [44, 20, 1], [44, 21, 1], [44, 23, 1], [44, 26, 1], [44, 32, 1], [44, 33, 1], [44, 35, 1], [44, 36, 1], [44, 38, 1], [44, 40, 1], [44, 41, 1], [44, 48, 1], [44, 49, 1], [44, 50, 1], [44, 53, 1], [44, 54, 1], [44, 57, 1], [44, 58, 1], [44, 65, 1], [44, 66, 1], [44, 67, 1], [44, 72, 1], [44, 79, 1], [44, 83, 1], [44, 85, 1], [44, 89, 1], [44, 92, 1], [44, 99, 1], [45, 4, 1], [45, 9, 1], [45, 14, 1], [45, 15, 1], [45, 16, 1], [45, 18, 1], [45, 19, 1], [45, 24, 1], [45, 27, 1], [45, 30, 1], [45, 33, 1], [45, 34, 1], [45, 35, 1], [45, 36, 1], [45, 40, 1], [45, 42, 1], [45, 48, 1], [45, 49, 1], [45, 54, 1], [45, 59, 1], [45, 67, 1], [45, 68, 1], [45, 71, 1], [45, 72, 1], [45, 73, 1], [45, 74, 1], [45, 85, 1], [45, 87, 1], [45, 88, 1], [45, 89, 1], [45, 90, 1], [45, 99, 1], [46, 7, 1], [46, 9, 1], [46, 12, 1], [46, 19, 1], [46, 30, 1], [46, 31, 1], [46, 33, 1], [46, 35, 1], [46, 39, 1], [46, 41, 1], [46, 42, 1], [46, 47, 1], [46, 49, 1], [46, 50, 1], [46, 53, 1], [46, 57, 1], [46, 58, 1], [46, 60, 1], [46, 63, 1], [46, 69, 1], [46, 70, 1], [46, 75, 1], [46, 78, 1], [46, 81, 1], [46, 87, 1], [46, 88, 1], [46, 91, 1], [46, 95, 1], [47, 0, 1], [47, 1, 1], [47, 11, 1], [47, 12, 1], [47, 13, 1], [47, 17, 1], [47, 18, 1], [47, 22, 1], [47, 25, 1], [47, 28, 1], [47, 31, 1], [47, 33, 1], [47, 34, 1], [47, 37, 1], [47, 39, 1], [47, 43, 1], [47, 46, 1], [47, 51, 1], [47, 52, 1], [47, 55, 1], [47, 60, 1], [47, 61, 1], [47, 65, 1], [47, 67, 1], [47, 70, 1], [47, 76, 1], [47, 81, 1], [47, 92, 1], [47, 94, 1], [47, 99, 1], [48, 1, 1], [48, 3, 1], [48, 4, 1], [48, 5, 1], [48, 11, 1], [48, 12, 1], [48, 13, 1], [48, 18, 1], [48, 23, 1], [48, 24, 1], [48, 33, 1], [48, 39, 1], [48, 44, 1], [48, 45, 1], [48, 50, 1], [48, 51, 1], [48, 52, 1], [48, 58, 1], [48, 64, 1], [48, 66, 1], [48, 67, 1], [48, 69, 1], [48, 74, 1], [48, 78, 1], [48, 80, 1], [48, 81, 1], [48, 87, 1], [48, 89, 1], [49, 2, 1], [49, 4, 1], [49, 5, 1], [49, 9, 1], [49, 14, 1], [49, 15, 1], [49, 20, 1], [49, 23, 1], [49, 27, 1], [49, 33, 1], [49, 34, 1], [49, 40, 1], [49, 41, 1], [49, 42, 1], [49, 43, 1], [49, 44, 1], [49, 45, 1], [49, 46, 1], [49, 50, 1], [49, 61, 1], [49, 65, 1], [49, 66, 1], [49, 68, 1], [49, 72, 1], [49, 79, 1], [49, 80, 1], [49, 85, 1], [49, 87, 1], [49, 92, 1], [49, 94, 1], [50, 2, 1], [50, 3, 1], [50, 6, 1], [50, 7, 1], [50, 8, 1], [50, 11, 1], [50, 25, 1], [50, 26, 1], [50, 29, 1], [50, 32, 1], [50, 36, 1], [50, 38, 1], [50, 41, 1], [50, 44, 1], [50, 46, 1], [50, 48, 1], [50, 49, 1], [50, 52, 1], [50, 56, 1], [50, 63, 1], [50, 69, 1], [50, 71, 1], [50, 78, 1], [50, 81, 1], [50, 85, 1], [50, 86, 1], [50, 88, 1], [50, 90, 1], [50, 91, 1], [50, 95, 1], [51, 0, 1], [51, 2, 1], [51, 4, 1], [51, 7, 1], [51, 8, 1], [51, 11, 1], [51, 18, 1], [51, 26, 1], [51, 35, 1], [51, 36, 1], [51, 39, 1], [51, 47, 1], [51, 48, 1], [51, 53, 1], [51, 54, 1], [51, 56, 1], [51, 59, 1], [51, 64, 1], [51, 71, 1], [51, 72, 1], [51, 73, 1], [51, 74, 1], [51, 77, 1], [51, 80, 1], [51, 82, 1], [51, 88, 1], [51, 91, 1], [51, 92, 1], [51, 97, 1], [52, 0, 1], [52, 1, 1], [52, 7, 1], [52, 8, 1], [52, 14, 1], [52, 22, 1], [52, 26, 1], [52, 32, 1], [52, 42, 1], [52, 43, 1], [52, 47, 1], [52, 48, 1], [52, 50, 1], [52, 59, 1], [52, 69, 1], [52, 71, 1], [52, 74, 1], [52, 75, 1], [52, 77, 1], [52, 83, 1], [52, 85, 1], [52, 87, 1], [52, 88, 1], [52, 91, 1], [52, 93, 1], [53, 0, 1], [53, 2, 1], [53, 5, 1], [53, 6, 1], [53, 10, 1], [53, 13, 1], [53, 16, 1], [53, 18, 1], [53, 22, 1], [53, 24, 1], [53, 29, 1], [53, 31, 1], [53, 33, 1], [53, 34, 1], [53, 44, 1], [53, 46, 1], [53, 51, 1], [53, 57, 1], [53, 59, 1], [53, 69, 1], [53, 72, 1], [53, 78, 1], [53, 82, 1], [53, 88, 1], [53, 89, 1], [53, 90, 1], [53, 93, 1], [53, 95, 1], [54, 0, 1], [54, 2, 1], [54, 3, 1], [54, 5, 1], [54, 6, 1], [54, 11, 1], [54, 12, 1], [54, 14, 1], [54, 17, 1], [54, 18, 1], [54, 21, 1], [54, 28, 1], [54, 36, 1], [54, 42, 1], [54, 43, 1], [54, 44, 1], [54, 45, 1], [54, 51, 1], [54, 55, 1], [54, 59, 1], [54, 68, 1], [54, 75, 1], [54, 77, 1], [54, 78, 1], [54, 80, 1], [54, 82, 1], [54, 86, 1], [54, 88, 1], [54, 89, 1], [54, 90, 1], [54, 94, 1], [54, 95, 1], [54, 97, 1], [54, 99, 1], [55, 0, 1], [55, 3, 1], [55, 4, 1], [55, 13, 1], [55, 16, 1], [55, 17, 1], [55, 22, 1], [55, 23, 1], [55, 29, 1], [55, 31, 1], [55, 33, 1], [55, 38, 1], [55, 40, 1], [55, 47, 1], [55, 54, 1], [55, 57, 1], [55, 60, 1], [55, 62, 1], [55, 63, 1], [55, 70, 1], [55, 71, 1], [55, 72, 1], [55, 73, 1], [55, 77, 1], [55, 82, 1], [55, 84, 1], [55, 85, 1], [55, 88, 1], [55, 93, 1], [55, 96, 1], [56, 4, 1], [56, 8, 1], [56, 11, 1], [56, 19, 1], [56, 26, 1], [56, 27, 1], [56, 29, 1], [56, 36, 1], [56, 41, 1], [56, 50, 1], [56, 51, 1], [56, 57, 1], [56, 60, 1], [56, 67, 1], [56, 73, 1], [56, 74, 1], [56, 77, 1], [56, 81, 1], [56, 83, 1], [56, 84, 1], [56, 85, 1], [56, 90, 1], [56, 92, 1], [56, 95, 1], [56, 97, 1], [56, 99, 1], [57, 7, 1], [57, 11, 1], [57, 12, 1], [57, 14, 1], [57, 15, 1], [57, 33, 1], [57, 34, 1], [57, 36, 1], [57, 40, 1], [57, 42, 1], [57, 44, 1], [57, 46, 1], [57, 53, 1], [57, 55, 1], [57, 56, 1], [57, 66, 1], [57, 67, 1], [57, 76, 1], [57, 77, 1], [57, 79, 1], [57, 80, 1], [57, 83, 1], [57, 89, 1], [57, 91, 1], [57, 92, 1], [57, 95, 1], [57, 98, 1], [57, 99, 1], [58, 10, 1], [58, 13, 1], [58, 15, 1], [58, 20, 1], [58, 24, 1], [58, 25, 1], [58, 29, 1], [58, 34, 1], [58, 36, 1], [58, 37, 1], [58, 38, 1], [58, 43, 1], [58, 44, 1], [58, 46, 1], [58, 48, 1], [58, 64, 1], [58, 66, 1], [58, 69, 1], [58, 71, 1], [58, 74, 1], [58, 78, 1], [58, 80, 1], [58, 82, 1], [58, 86, 1], [58, 87, 1], [58, 89, 1], [58, 93, 1], [59, 0, 1], [59, 1, 1], [59, 4, 1], [59, 6, 1], [59, 18, 1], [59, 24, 1], [59, 27, 1], [59, 30, 1], [59, 33, 1], [59, 36, 1], [59, 45, 1], [59, 51, 1], [59, 52, 1], [59, 53, 1], [59, 54, 1], [59, 61, 1], [59, 62, 1], [59, 65, 1], [59, 74, 1], [59, 76, 1], [59, 77, 1], [59, 83, 1], [59, 84, 1], [59, 90, 1], [59, 91, 1], [59, 92, 1], [59, 93, 1], [59, 95, 1], [59, 97, 1], [59, 99, 1], [60, 3, 1], [60, 6, 1], [60, 8, 1], [60, 12, 1], [60, 15, 1], [60, 16, 1], [60, 19, 1], [60, 21, 1], [60, 25, 1], [60, 26, 1], [60, 28, 1], [60, 29, 1], [60, 32, 1], [60, 35, 1], [60, 37, 1], [60, 39, 1], [60, 40, 1], [60, 43, 1], [60, 46, 1], [60, 47, 1], [60, 55, 1], [60, 56, 1], [60, 66, 1], [60, 68, 1], [60, 69, 1], [60, 70, 1], [60, 73, 1], [60, 78, 1], [60, 79, 1], [60, 89, 1], [60, 91, 1], [60, 92, 1], [60, 94, 1], [60, 95, 1], [60, 99, 1], [61, 0, 1], [61, 9, 1], [61, 21, 1], [61, 28, 1], [61, 32, 1], [61, 36, 1], [61, 39, 1], [61, 42, 1], [61, 47, 1], [61, 49, 1], [61, 59, 1], [61, 65, 1], [61, 68, 1], [61, 71, 1], [61, 72, 1], [61, 74, 1], [61, 76, 1], [61, 85, 1], [61, 88, 1], [61, 96, 1], [62, 0, 1], [62, 1, 1], [62, 6, 1], [62, 10, 1], [62, 12, 1], [62, 14, 1], [62, 18, 1], [62, 25, 1], [62, 40, 1], [62, 43, 1], [62, 55, 1], [62, 59, 1], [62, 70, 1], [62, 79, 1], [62, 81, 1], [62, 84, 1], [62, 86, 1], [62, 88, 1], [62, 94, 1], [62, 98, 1], [63, 8, 1], [63, 9, 1], [63, 13, 1], [63, 14, 1], [63, 18, 1], [63, 24, 1], [63, 25, 1], [63, 27, 1], [63, 28, 1], [63, 30, 1], [63, 37, 1], [63, 39, 1], [63, 41, 1], [63, 46, 1], [63, 50, 1], [63, 55, 1], [63, 66, 1], [63, 67, 1], [63, 72, 1], [63, 75, 1], [63, 79, 1], [63, 81, 1], [63, 84, 1], [63, 86, 1], [63, 88, 1], [63, 92, 1], [63, 95, 1], [63, 96, 1], [64, 7, 1], [64, 8, 1], [64, 11, 1], [64, 13, 1], [64, 14, 1], [64, 16, 1], [64, 18, 1], [64, 19, 1], [64, 20, 1], [64, 22, 1], [64, 25, 1], [64, 27, 1], [64, 30, 1], [64, 33, 1], [64, 35, 1], [64, 37, 1], [64, 39, 1], [64, 48, 1], [64, 51, 1], [64, 58, 1], [64, 67, 1], [64, 68, 1], [64, 77, 1], [64, 81, 1], [64, 82, 1], [64, 89, 1], [64, 94, 1], [64, 99, 1], [65, 3, 1], [65, 5, 1], [65, 7, 1], [65, 9, 1], [65, 12, 1], [65, 18, 1], [65, 26, 1], [65, 27, 1], [65, 30, 1], [65, 34, 1], [65, 35, 1], [65, 44, 1], [65, 47, 1], [65, 49, 1], [65, 59, 1], [65, 61, 1], [65, 67, 1], [65, 70, 1], [65, 73, 1], [65, 75, 1], [65, 83, 1], [65, 86, 1], [65, 88, 1], [65, 90, 1], [65, 93, 1], [65, 96, 1], [65, 99, 1], [66, 2, 1], [66, 3, 1], [66, 4, 1], [66, 6, 1], [66, 7, 1], [66, 8, 1], [66, 11, 1], [66, 12, 1], [66, 17, 1], [66, 23, 1], [66, 24, 1], [66, 26, 1], [66, 28, 1], [66, 33, 1], [66, 35, 1], [66, 36, 1], [66, 37, 1], [66, 38, 1], [66, 43, 1], [66, 44, 1], [66, 48, 1], [66, 49, 1], [66, 57, 1], [66, 58, 1], [66, 60, 1], [66, 63, 1], [66, 73, 1], [66, 75, 1], [66, 79, 1], [66, 92, 1], [66, 93, 1], [66, 99, 1], [67, 0, 1], [67, 2, 1], [67, 5, 1], [67, 15, 1], [67, 18, 1], [67, 19, 1], [67, 20, 1], [67, 22, 1], [67, 32, 1], [67, 33, 1], [67, 35, 1], [67, 40, 1], [67, 41, 1], [67, 44, 1], [67, 45, 1], [67, 47, 1], [67, 48, 1], [67, 56, 1], [67, 57, 1], [67, 63, 1], [67, 64, 1], [67, 65, 1], [67, 77, 1], [67, 79, 1], [67, 88, 1], [67, 89, 1], [67, 91, 1], [68, 1, 1], [68, 5, 1], [68, 8, 1], [68, 9, 1], [68, 19, 1], [68, 20, 1], [68, 22, 1], [68, 23, 1], [68, 28, 1], [68, 34, 1], [68, 36, 1], [68, 41, 1], [68, 45, 1], [68, 49, 1], [68, 54, 1], [68, 60, 1], [68, 61, 1], [68, 64, 1], [68, 73, 1], [68, 75, 1], [68, 77, 1], [68, 80, 1], [68, 82, 1], [68, 85, 1], [68, 86, 1], [68, 95, 1], [69, 0, 1], [69, 1, 1], [69, 2, 1], [69, 5, 1], [69, 8, 1], [69, 10, 1], [69, 11, 1], [69, 16, 1], [69, 17, 1], [69, 18, 1], [69, 20, 1], [69, 21, 1], [69, 22, 1], [69, 23, 1], [69, 26, 1], [69, 41, 1], [69, 46, 1], [69, 48, 1], [69, 50, 1], [69, 52, 1], [69, 53, 1], [69, 58, 1], [69, 60, 1], [69, 71, 1], [69, 72, 1], [69, 75, 1], [69, 80, 1], [69, 87, 1], [69, 91, 1], [70, 0, 1], [70, 4, 1], [70, 14, 1], [70, 15, 1], [70, 19, 1], [70, 23, 1], [70, 28, 1], [70, 32, 1], [70, 46, 1], [70, 47, 1], [70, 55, 1], [70, 60, 1], [70, 62, 1], [70, 65, 1], [70, 75, 1], [70, 77, 1], [70, 78, 1], [70, 81, 1], [70, 82, 1], [70, 87, 1], [70, 91, 1], [70, 92, 1], [70, 96, 1], [71, 4, 1], [71, 10, 1], [71, 13, 1], [71, 17, 1], [71, 18, 1], [71, 19, 1], [71, 26, 1], [71, 29, 1], [71, 30, 1], [71, 34, 1], [71, 38, 1], [71, 39, 1], [71, 45, 1], [71, 50, 1], [71, 51, 1], [71, 52, 1], [71, 55, 1], [71, 58, 1], [71, 61, 1], [71, 69, 1], [71, 73, 1], [71, 74, 1], [71, 79, 1], [71, 80, 1], [71, 82, 1], [71, 84, 1], [71, 85, 1], [71, 86, 1], [71, 88, 1], [71, 91, 1], [71, 93, 1], [71, 97, 1], [71, 98, 1], [72, 17, 1], [72, 19, 1], [72, 21, 1], [72, 22, 1], [72, 25, 1], [72, 27, 1], [72, 28, 1], [72, 34, 1], [72, 41, 1], [72, 44, 1], [72, 45, 1], [72, 49, 1], [72, 51, 1], [72, 53, 1], [72, 55, 1], [72, 61, 1], [72, 63, 1], [72, 69, 1], [72, 75, 1], [72, 83, 1], [72, 84, 1], [72, 92, 1], [72, 94, 1], [73, 4, 1], [73, 6, 1], [73, 15, 1], [73, 23, 1], [73, 25, 1], [73, 38, 1], [73, 40, 1], [73, 43, 1], [73, 45, 1], [73, 51, 1], [73, 55, 1], [73, 56, 1], [73, 60, 1], [73, 65, 1], [73, 66, 1], [73, 68, 1], [73, 71, 1], [73, 76, 1], [73, 78, 1], [73, 84, 1], [73, 87, 1], [73, 94, 1], [73, 95, 1], [73, 98, 1], [74, 0, 1], [74, 2, 1], [74, 3, 1], [74, 4, 1], [74, 8, 1], [74, 9, 1], [74, 10, 1], [74, 11, 1], [74, 14, 1], [74, 16, 1], [74, 19, 1], [74, 22, 1], [74, 26, 1], [74, 32, 1], [74, 34, 1], [74, 37, 1], [74, 42, 1], [74, 45, 1], [74, 48, 1], [74, 51, 1], [74, 52, 1], [74, 56, 1], [74, 58, 1], [74, 59, 1], [74, 61, 1], [74, 71, 1], [74, 78, 1], [74, 80, 1], [74, 86, 1], [74, 87, 1], [74, 92, 1], [74, 97, 1], [75, 12, 1], [75, 14, 1], [75, 18, 1], [75, 19, 1], [75, 20, 1], [75, 22, 1], [75, 23, 1], [75, 31, 1], [75, 32, 1], [75, 33, 1], [75, 35, 1], [75, 37, 1], [75, 39, 1], [75, 40, 1], [75, 46, 1], [75, 52, 1], [75, 54, 1], [75, 63, 1], [75, 65, 1], [75, 66, 1], [75, 68, 1], [75, 69, 1], [75, 70, 1], [75, 72, 1], [75, 79, 1], [75, 80, 1], [75, 83, 1], [75, 92, 1], [75, 97, 1], [76, 2, 1], [76, 4, 1], [76, 5, 1], [76, 15, 1], [76, 18, 1], [76, 20, 1], [76, 22, 1], [76, 23, 1], [76, 26, 1], [76, 28, 1], [76, 33, 1], [76, 35, 1], [76, 37, 1], [76, 39, 1], [76, 40, 1], [76, 47, 1], [76, 57, 1], [76, 59, 1], [76, 61, 1], [76, 73, 1], [76, 77, 1], [76, 78, 1], [76, 80, 1], [76, 81, 1], [76, 84, 1], [76, 90, 1], [76, 96, 1], [77, 1, 1], [77, 3, 1], [77, 4, 1], [77, 6, 1], [77, 8, 1], [77, 11, 1], [77, 12, 1], [77, 14, 1], [77, 16, 1], [77, 17, 1], [77, 18, 1], [77, 24, 1], [77, 27, 1], [77, 35, 1], [77, 36, 1], [77, 37, 1], [77, 39, 1], [77, 41, 1], [77, 43, 1], [77, 51, 1], [77, 52, 1], [77, 54, 1], [77, 55, 1], [77, 56, 1], [77, 57, 1], [77, 59, 1], [77, 64, 1], [77, 67, 1], [77, 68, 1], [77, 70, 1], [77, 76, 1], [77, 83, 1], [77, 86, 1], [77, 88, 1], [77, 96, 1], [78, 2, 1], [78, 13, 1], [78, 16, 1], [78, 17, 1], [78, 25, 1], [78, 33, 1], [78, 34, 1], [78, 36, 1], [78, 39, 1], [78, 42, 1], [78, 46, 1], [78, 48, 1], [78, 50, 1], [78, 53, 1], [78, 54, 1], [78, 58, 1], [78, 60, 1], [78, 70, 1], [78, 73, 1], [78, 74, 1], [78, 76, 1], [78, 84, 1], [78, 86, 1], [78, 89, 1], [78, 94, 1], [78, 96, 1], [79, 2, 1], [79, 7, 1], [79, 13, 1], [79, 17, 1], [79, 19, 1], [79, 33, 1], [79, 36, 1], [79, 37, 1], [79, 38, 1], [79, 44, 1], [79, 49, 1], [79, 57, 1], [79, 60, 1], [79, 62, 1], [79, 63, 1], [79, 66, 1], [79, 67, 1], [79, 71, 1], [79, 75, 1], [79, 81, 1], [79, 86, 1], [79, 89, 1], [79, 94, 1], [79, 96, 1], [79, 97, 1], [80, 5, 1], [80, 6, 1], [80, 7, 1], [80, 10, 1], [80, 13, 1], [80, 14, 1], [80, 18, 1], [80, 21, 1], [80, 28, 1], [80, 30, 1], [80, 31, 1], [80, 37, 1], [80, 38, 1], [80, 39, 1], [80, 43, 1], [80, 48, 1], [80, 49, 1], [80, 51, 1], [80, 54, 1], [80, 57, 1], [80, 58, 1], [80, 68, 1], [80, 69, 1], [80, 71, 1], [80, 74, 1], [80, 75, 1], [80, 76, 1], [80, 82, 1], [80, 83, 1], [80, 90, 1], [80, 94, 1], [80, 95, 1], [81, 1, 1], [81, 5, 1], [81, 6, 1], [81, 11, 1], [81, 14, 1], [81, 20, 1], [81, 21, 1], [81, 22, 1], [81, 23, 1], [81, 31, 1], [81, 32, 1], [81, 33, 1], [81, 35, 1], [81, 37, 1], [81, 39, 1], [81, 41, 1], [81, 46, 1], [81, 47, 1], [81, 48, 1], [81, 50, 1], [81, 56, 1], [81, 62, 1], [81, 63, 1], [81, 64, 1], [81, 70, 1], [81, 76, 1], [81, 79, 1], [81, 85, 1], [81, 88, 1], [81, 90, 1], [81, 96, 1], [81, 97, 1], [82, 2, 1], [82, 3, 1], [82, 4, 1], [82, 6, 1], [82, 7, 1], [82, 8, 1], [82, 9, 1], [82, 11, 1], [82, 14, 1], [82, 17, 1], [82, 18, 1], [82, 23, 1], [82, 28, 1], [82, 32, 1], [82, 34, 1], [82, 40, 1], [82, 42, 1], [82, 51, 1], [82, 53, 1], [82, 54, 1], [82, 55, 1], [82, 58, 1], [82, 64, 1], [82, 68, 1], [82, 70, 1], [82, 71, 1], [82, 80, 1], [82, 93, 1], [82, 95, 1], [82, 99, 1], [83, 0, 1], [83, 1, 1], [83, 2, 1], [83, 3, 1], [83, 7, 1], [83, 16, 1], [83, 19, 1], [83, 20, 1], [83, 21, 1], [83, 22, 1], [83, 27, 1], [83, 40, 1], [83, 42, 1], [83, 44, 1], [83, 52, 1], [83, 56, 1], [83, 57, 1], [83, 59, 1], [83, 65, 1], [83, 72, 1], [83, 75, 1], [83, 77, 1], [83, 80, 1], [83, 84, 1], [83, 85, 1], [83, 93, 1], [83, 94, 1], [84, 3, 1], [84, 9, 1], [84, 10, 1], [84, 14, 1], [84, 16, 1], [84, 26, 1], [84, 29, 1], [84, 30, 1], [84, 32, 1], [84, 35, 1], [84, 38, 1], [84, 39, 1], [84, 41, 1], [84, 55, 1], [84, 56, 1], [84, 59, 1], [84, 62, 1], [84, 63, 1], [84, 71, 1], [84, 72, 1], [84, 73, 1], [84, 76, 1], [84, 78, 1], [84, 83, 1], [84, 85, 1], [84, 88, 1], [84, 91, 1], [84, 94, 1], [84, 98, 1], [85, 1, 1], [85, 7, 1], [85, 8, 1], [85, 12, 1], [85, 17, 1], [85, 18, 1], [85, 20, 1], [85, 23, 1], [85, 24, 1], [85, 25, 1], [85, 28, 1], [85, 29, 1], [85, 37, 1], [85, 41, 1], [85, 44, 1], [85, 45, 1], [85, 49, 1], [85, 50, 1], [85, 52, 1], [85, 55, 1], [85, 56, 1], [85, 61, 1], [85, 68, 1], [85, 71, 1], [85, 81, 1], [85, 83, 1], [85, 84, 1], [85, 88, 1], [85, 98, 1], [86, 0, 1], [86, 1, 1], [86, 3, 1], [86, 5, 1], [86, 6, 1], [86, 10, 1], [86, 14, 1], [86, 15, 1], [86, 21, 1], [86, 29, 1], [86, 34, 1], [86, 35, 1], [86, 36, 1], [86, 37, 1], [86, 38, 1], [86, 40, 1], [86, 41, 1], [86, 42, 1], [86, 43, 1], [86, 50, 1], [86, 54, 1], [86, 58, 1], [86, 62, 1], [86, 63, 1], [86, 65, 1], [86, 68, 1], [86, 71, 1], [86, 74, 1], [86, 77, 1], [86, 78, 1], [86, 79, 1], [86, 91, 1], [86, 98, 1], [87, 2, 1], [87, 3, 1], [87, 9, 1], [87, 13, 1], [87, 24, 1], [87, 31, 1], [87, 33, 1], [87, 36, 1], [87, 39, 1], [87, 41, 1], [87, 45, 1], [87, 46, 1], [87, 48, 1], [87, 49, 1], [87, 52, 1], [87, 58, 1], [87, 69, 1], [87, 70, 1], [87, 73, 1], [87, 74, 1], [87, 89, 1], [87, 98, 1], [87, 99, 1], [88, 0, 1], [88, 5, 1], [88, 6, 1], [88, 8, 1], [88, 9, 1], [88, 15, 1], [88, 17, 1], [88, 18, 1], [88, 25, 1], [88, 28, 1], [88, 31, 1], [88, 37, 1], [88, 38, 1], [88, 41, 1], [88, 45, 1], [88, 46, 1], [88, 50, 1], [88, 51, 1], [88, 52, 1], [88, 53, 1], [88, 54, 1], [88, 55, 1], [88, 61, 1], [88, 62, 1], [88, 63, 1], [88, 65, 1], [88, 67, 1], [88, 71, 1], [88, 77, 1], [88, 81, 1], [88, 84, 1], [88, 85, 1], [88, 89, 1], [88, 92, 1], [88, 96, 1], [88, 98, 1], [89, 6, 1], [89, 10, 1], [89, 16, 1], [89, 18, 1], [89, 19, 1], [89, 22, 1], [89, 23, 1], [89, 26, 1], [89, 28, 1], [89, 31, 1], [89, 33, 1], [89, 42, 1], [89, 43, 1], [89, 44, 1], [89, 45, 1], [89, 48, 1], [89, 53, 1], [89, 54, 1], [89, 57, 1], [89, 58, 1], [89, 60, 1], [89, 64, 1], [89, 67, 1], [89, 78, 1], [89, 79, 1], [89, 87, 1], [89, 88, 1], [89, 92, 1], [89, 96, 1], [90, 3, 1], [90, 4, 1], [90, 5, 1], [90, 7, 1], [90, 9, 1], [90, 18, 1], [90, 20, 1], [90, 26, 1], [90, 33, 1], [90, 36, 1], [90, 37, 1], [90, 43, 1], [90, 45, 1], [90, 50, 1], [90, 53, 1], [90, 54, 1], [90, 56, 1], [90, 59, 1], [90, 65, 1], [90, 76, 1], [90, 80, 1], [90, 81, 1], [90, 92, 1], [90, 94, 1], [90, 96, 1], [91, 6, 1], [91, 8, 1], [91, 11, 1], [91, 15, 1], [91, 17, 1], [91, 18, 1], [91, 25, 1], [91, 26, 1], [91, 30, 1], [91, 32, 1], [91, 33, 1], [91, 35, 1], [91, 37, 1], [91, 39, 1], [91, 46, 1], [91, 50, 1], [91, 51, 1], [91, 52, 1], [91, 57, 1], [91, 59, 1], [91, 60, 1], [91, 67, 1], [91, 69, 1], [91, 70, 1], [91, 71, 1], [91, 84, 1], [91, 86, 1], [91, 97, 1], [91, 98, 1], [92, 0, 1], [92, 1, 1], [92, 2, 1], [92, 6, 1], [92, 8, 1], [92, 16, 1], [92, 17, 1], [92, 21, 1], [92, 23, 1], [92, 24, 1], [92, 25, 1], [92, 32, 1], [92, 33, 1], [92, 36, 1], [92, 37, 1], [92, 38, 1], [92, 40, 1], [92, 44, 1], [92, 47, 1], [92, 49, 1], [92, 51, 1], [92, 56, 1], [92, 57, 1], [92, 59, 1], [92, 60, 1], [92, 63, 1], [92, 66, 1], [92, 70, 1], [92, 72, 1], [92, 74, 1], [92, 75, 1], [92, 88, 1], [92, 89, 1], [92, 90, 1], [92, 97, 1], [93, 3, 1], [93, 6, 1], [93, 7, 1], [93, 8, 1], [93, 10, 1], [93, 15, 1], [93, 17, 1], [93, 18, 1], [93, 19, 1], [93, 20, 1], [93, 23, 1], [93, 36, 1], [93, 37, 1], [93, 39, 1], [93, 43, 1], [93, 52, 1], [93, 53, 1], [93, 55, 1], [93, 58, 1], [93, 59, 1], [93, 65, 1], [93, 66, 1], [93, 71, 1], [93, 82, 1], [93, 83, 1], [93, 95, 1], [93, 98, 1], [94, 2, 1], [94, 4, 1], [94, 10, 1], [94, 11, 1], [94, 16, 1], [94, 17, 1], [94, 19, 1], [94, 20, 1], [94, 29, 1], [94, 30, 1], [94, 32, 1], [94, 35, 1], [94, 37, 1], [94, 43, 1], [94, 47, 1], [94, 49, 1], [94, 54, 1], [94, 60, 1], [94, 62, 1], [94, 64, 1], [94, 72, 1], [94, 73, 1], [94, 78, 1], [94, 79, 1], [94, 80, 1], [94, 83, 1], [94, 84, 1], [94, 90, 1], [94, 97, 1], [94, 98, 1], [94, 99, 1], [95, 0, 1], [95, 2, 1], [95, 5, 1], [95, 6, 1], [95, 8, 1], [95, 13, 1], [95, 16, 1], [95, 19, 1], [95, 22, 1], [95, 27, 1], [95, 28, 1], [95, 38, 1], [95, 39, 1], [95, 42, 1], [95, 46, 1], [95, 50, 1], [95, 53, 1], [95, 54, 1], [95, 56, 1], [95, 57, 1], [95, 59, 1], [95, 60, 1], [95, 63, 1], [95, 68, 1], [95, 73, 1], [95, 80, 1], [95, 82, 1], [95, 93, 1], [95, 97, 1], [96, 0, 1], [96, 3, 1], [96, 4, 1], [96, 5, 1], [96, 11, 1], [96, 13, 1], [96, 16, 1], [96, 21, 1], [96, 26, 1], [96, 27, 1], [96, 30, 1], [96, 31, 1], [96, 32, 1], [96, 33, 1], [96, 38, 1], [96, 41, 1], [96, 55, 1], [96, 61, 1], [96, 63, 1], [96, 65, 1], [96, 70, 1], [96, 76, 1], [96, 77, 1], [96, 78, 1], [96, 79, 1], [96, 81, 1], [96, 88, 1], [96, 89, 1], [96, 90, 1], [97, 3, 1], [97, 4, 1], [97, 6, 1], [97, 12, 1], [97, 14, 1], [97, 15, 1], [97, 16, 1], [97, 18, 1], [97, 19, 1], [97, 24, 1], [97, 27, 1], [97, 29, 1], [97, 33, 1], [97, 34, 1], [97, 37, 1], [97, 42, 1], [97, 51, 1], [97, 54, 1], [97, 56, 1], [97, 59, 1], [97, 71, 1], [97, 74, 1], [97, 75, 1], [97, 79, 1], [97, 81, 1], [97, 91, 1], [97, 92, 1], [97, 94, 1], [97, 95, 1], [97, 98, 1], [98, 0, 1], [98, 4, 1], [98, 6, 1], [98, 7, 1], [98, 9, 1], [98, 12, 1], [98, 15, 1], [98, 17, 1], [98, 18, 1], [98, 20, 1], [98, 21, 1], [98, 22, 1], [98, 26, 1], [98, 27, 1], [98, 28, 1], [98, 34, 1], [98, 38, 1], [98, 39, 1], [98, 40, 1], [98, 57, 1], [98, 62, 1], [98, 71, 1], [98, 73, 1], [98, 84, 1], [98, 85, 1], [98, 86, 1], [98, 87, 1], [98, 88, 1], [98, 91, 1], [98, 93, 1], [98, 94, 1], [98, 97, 1], [99, 1, 1], [99, 4, 1], [99, 9, 1], [99, 14, 1], [99, 15, 1], [99, 16, 1], [99, 19, 1], [99, 21, 1], [99, 22, 1], [99, 24, 1], [99, 31, 1], [99, 32, 1], [99, 44, 1], [99, 45, 1], [99, 47, 1], [99, 54, 1], [99, 56, 1], [99, 57, 1], [99, 59, 1], [99, 60, 1], [99, 64, 1], [99, 65, 1], [99, 66, 1], [99, 82, 1], [99, 87, 1], [99, 94, 1]]

matrix_raw = np.zeros((100, 100))
# Loop through the list of tuples and set corresponding positions to 1
for pos in lst:
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
for i in range(100):
    for j in range(i+1, 100):
        if matrix[i][j] < 0.0:
            J[(i, j)] = 1.0
        #else:
          #  J[(i, j)] = -1.0


# Create an empty array
my_array = []







final_time=0

for i in range(1000):
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
average_y = np.mean(y)

# Print the average of the y-coordinates
print("The average of the y-axis values is:", average_y)


# print energy of first solution
print(sampleset.first.energy)


# Show the plot
plt.show()