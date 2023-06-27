#Use this version for all testing of full matrix (100 nodes)
# write a program that that uses simulated annealing to solve max-cut
import random
import math
import itertools
import numpy as np
#partition basically separates the points into separate groups of 0's and 1's starting from [0,0,0,0,1]


# Define the graph as an adjacency matrix
lst =  [[0, 12, 1], [0, 15, 1], [0, 53, 1], [0, 90, 1], [1, 27, 1], [1, 42, 1], [1, 65, 1], [1, 69, 1], [1, 76, 1], [1, 82, 1], [1, 83, 1], [1, 85, 1], [1, 97, 1], [2, 12, 1], [2, 37, 1], [2, 39, 1], [2, 60, 1], [2, 67, 1], [2, 72, 1], [2, 82, 1], [2, 86, 1], [2, 87, 1], [2, 88, 1], [2, 98, 1], [3, 17, 1], [3, 24, 1], [3, 31, 1], [3, 46, 1], [3, 55, 1], [3, 62, 1], [3, 77, 1], [3, 79, 1], [3, 82, 1], [3, 83, 1], [3, 86, 1], [3, 92, 1], [3, 94, 1], [3, 98, 1], [4, 6, 1], [4, 9, 1], [4, 11, 1], [4, 26, 1], [4, 27, 1], [4, 28, 1], [4, 33, 1], [4, 39, 1], [4, 41, 1], [4, 48, 1], [4, 51, 1], [4, 60, 1], [4, 65, 1], [4, 72, 1], [4, 81, 1], [4, 82, 1], [4, 87, 1], [5, 43, 1], [5, 47, 1], [5, 48, 1], [5, 51, 1], [5, 60, 1], [5, 61, 1], [5, 81, 1], [5, 86, 1], [5, 89, 1], [5, 99, 1], [6, 4, 1], [6, 15, 1], [6, 23, 1], [6, 36, 1], [6, 42, 1], [6, 60, 1], [6, 61, 1], [6, 66, 1], [6, 72, 1], [6, 77, 1], [6, 78, 1], [6, 85, 1], [6, 92, 1], [7, 24, 1], [7, 74, 1], [7, 85, 1], [7, 94, 1], [8, 19, 1], [8, 47, 1], [8, 62, 1], [8, 66, 1], [8, 70, 1], [8, 72, 1], [8, 75, 1], [8, 92, 1], [8, 94, 1], [8, 97, 1], [9, 4, 1], [9, 10, 1], [9, 14, 1], [9, 29, 1], [9, 42, 1], [9, 47, 1], [9, 49, 1], [9, 52, 1], [9, 64, 1], [9, 68, 1], [9, 85, 1], [9, 92, 1], [9, 94, 1], [10, 9, 1], [10, 22, 1], [10, 26, 1], [10, 28, 1], [10, 34, 1], [10, 45, 1], [10, 61, 1], [10, 76, 1], [10, 85, 1], [10, 86, 1], [10, 96, 1], [11, 4, 1], [11, 14, 1], [11, 17, 1], [11, 21, 1], [11, 26, 1], [11, 40, 1], [11, 58, 1], [11, 63, 1], [11, 69, 1], [11, 70, 1], [11, 74, 1], [11, 78, 1], [11, 87, 1], [11, 96, 1], [12, 0, 1], [12, 2, 1], [12, 34, 1], [12, 37, 1], [12, 39, 1], [12, 42, 1], [12, 61, 1], [12, 68, 1], [12, 83, 1], [12, 90, 1], [13, 16, 1], [13, 19, 1], [13, 25, 1], [13, 35, 1], [13, 40, 1], [13, 47, 1], [13, 57, 1], [13, 60, 1], [13, 63, 1], [13, 74, 1], [13, 82, 1], [14, 9, 1], [14, 11, 1], [14, 16, 1], [14, 32, 1], [14, 37, 1], [14, 40, 1], [14, 49, 1], [15, 0, 1], [15, 6, 1], [15, 33, 1], [15, 39, 1], [15, 76, 1], [16, 13, 1], [16, 14, 1], [16, 21, 1], [16, 50, 1], [16, 59, 1], [16, 65, 1], [16, 67, 1], [16, 94, 1], [16, 95, 1], [17, 3, 1], [17, 11, 1], [17, 28, 1], [17, 32, 1], [17, 35, 1], [17, 40, 1], [17, 83, 1], [17, 84, 1], [17, 90, 1], [17, 91, 1], [18, 33, 1], [18, 66, 1], [18, 68, 1], [18, 70, 1], [18, 74, 1], [18, 85, 1], [18, 91, 1], [18, 92, 1], [19, 8, 1], [19, 13, 1], [19, 43, 1], [19, 50, 1], [19, 61, 1], [19, 63, 1], [19, 80, 1], [19, 93, 1], [20, 26, 1], [20, 35, 1], [20, 37, 1], [20, 45, 1], [20, 46, 1], [20, 47, 1], [20, 48, 1], [20, 56, 1], [20, 63, 1], [20, 66, 1], [20, 74, 1], [21, 11, 1], [21, 16, 1], [21, 25, 1], [21, 30, 1], [21, 33, 1], [21, 35, 1], [21, 37, 1], [21, 38, 1], [21, 40, 1], [21, 49, 1], [21, 62, 1], [21, 96, 1], [22, 10, 1], [22, 54, 1], [22, 64, 1], [22, 66, 1], [22, 71, 1], [22, 88, 1], [22, 99, 1], [23, 6, 1], [23, 38, 1], [23, 41, 1], [23, 42, 1], [23, 47, 1], [23, 55, 1], [23, 66, 1], [23, 81, 1], [23, 92, 1], [24, 3, 1], [24, 7, 1], [24, 30, 1], [24, 43, 1], [24, 46, 1], [24, 54, 1], [24, 62, 1], [24, 75, 1], [24, 89, 1], [24, 96, 1], [25, 13, 1], [25, 21, 1], [25, 35, 1], [25, 62, 1], [25, 90, 1], [26, 4, 1], [26, 10, 1], [26, 11, 1], [26, 20, 1], [26, 31, 1], [26, 43, 1], [26, 69, 1], [26, 73, 1], [26, 84, 1], [27, 1, 1], [27, 4, 1], [27, 46, 1], [27, 47, 1], [27, 51, 1], [27, 63, 1], [27, 80, 1], [27, 94, 1], [27, 96, 1], [27, 98, 1], [28, 4, 1], [28, 10, 1], [28, 17, 1], [28, 29, 1], [28, 44, 1], [28, 47, 1], [28, 50, 1], [28, 72, 1], [28, 78, 1], [28, 88, 1], [28, 91, 1], [28, 99, 1], [29, 9, 1], [29, 28, 1], [29, 30, 1], [29, 48, 1], [29, 51, 1], [29, 57, 1], [29, 67, 1], [29, 92, 1], [29, 97, 1], [30, 21, 1], [30, 24, 1], [30, 29, 1], [30, 39, 1], [30, 43, 1], [30, 57, 1], [30, 60, 1], [30, 65, 1], [31, 3, 1], [31, 26, 1], [31, 47, 1], [31, 48, 1], [31, 53, 1], [31, 66, 1], [31, 91, 1], [31, 95, 1], [32, 14, 1], [32, 17, 1], [32, 36, 1], [32, 40, 1], [32, 55, 1], [32, 59, 1], [32, 72, 1], [32, 92, 1], [33, 4, 1], [33, 15, 1], [33, 18, 1], [33, 21, 1], [33, 38, 1], [33, 40, 1], [33, 46, 1], [33, 48, 1], [33, 49, 1], [33, 54, 1], [33, 77, 1], [33, 83, 1], [33, 85, 1], [33, 86, 1], [33, 87, 1], [34, 10, 1], [34, 12, 1], [34, 48, 1], [34, 56, 1], [34, 63, 1], [34, 81, 1], [34, 83, 1], [34, 90, 1], [34, 96, 1], [35, 13, 1], [35, 17, 1], [35, 20, 1], [35, 21, 1], [35, 25, 1], [35, 42, 1], [35, 51, 1], [35, 75, 1], [36, 6, 1], [36, 32, 1], [36, 50, 1], [36, 53, 1], [36, 55, 1], [36, 61, 1], [36, 62, 1], [36, 77, 1], [36, 80, 1], [36, 98, 1], [37, 2, 1], [37, 12, 1], [37, 14, 1], [37, 20, 1], [37, 21, 1], [37, 42, 1], [37, 55, 1], [37, 60, 1], [37, 62, 1], [37, 71, 1], [37, 82, 1], [37, 85, 1], [37, 89, 1], [37, 95, 1], [38, 21, 1], [38, 23, 1], [38, 33, 1], [38, 60, 1], [38, 78, 1], [39, 2, 1], [39, 4, 1], [39, 12, 1], [39, 15, 1], [39, 30, 1], [39, 42, 1], [39, 48, 1], [39, 51, 1], [39, 58, 1], [39, 70, 1], [39, 76, 1], [39, 79, 1], [39, 86, 1], [40, 11, 1], [40, 13, 1], [40, 14, 1], [40, 17, 1], [40, 21, 1], [40, 32, 1], [40, 33, 1], [40, 49, 1], [40, 53, 1], [40, 57, 1], [40, 63, 1], [40, 75, 1], [40, 88, 1], [41, 4, 1], [41, 23, 1], [41, 74, 1], [42, 1, 1], [42, 6, 1], [42, 9, 1], [42, 12, 1], [42, 23, 1], [42, 35, 1], [42, 37, 1], [42, 39, 1], [42, 57, 1], [42, 75, 1], [42, 76, 1], [42, 82, 1], [42, 87, 1], [43, 5, 1], [43, 19, 1], [43, 24, 1], [43, 26, 1], [43, 30, 1], [43, 44, 1], [43, 48, 1], [43, 56, 1], [43, 63, 1], [43, 65, 1], [43, 75, 1], [43, 77, 1], [43, 95, 1], [44, 28, 1], [44, 43, 1], [44, 60, 1], [44, 75, 1], [44, 78, 1], [44, 83, 1], [44, 85, 1], [45, 10, 1], [45, 20, 1], [45, 52, 1], [45, 53, 1], [45, 67, 1], [45, 73, 1], [45, 75, 1], [45, 81, 1], [45, 91, 1], [46, 3, 1], [46, 20, 1], [46, 24, 1], [46, 27, 1], [46, 33, 1], [46, 49, 1], [46, 51, 1], [46, 53, 1], [46, 57, 1], [46, 66, 1], [46, 73, 1], [46, 78, 1], [46, 80, 1], [46, 83, 1], [46, 88, 1], [47, 5, 1], [47, 8, 1], [47, 9, 1], [47, 13, 1], [47, 20, 1], [47, 23, 1], [47, 27, 1], [47, 28, 1], [47, 31, 1], [47, 56, 1], [47, 58, 1], [47, 91, 1], [47, 92, 1], [47, 93, 1], [47, 99, 1], [48, 4, 1], [48, 5, 1], [48, 20, 1], [48, 29, 1], [48, 31, 1], [48, 33, 1], [48, 34, 1], [48, 39, 1], [48, 43, 1], [48, 55, 1], [48, 76, 1], [48, 91, 1], [48, 98, 1], [48, 99, 1], [49, 9, 1], [49, 14, 1], [49, 21, 1], [49, 33, 1], [49, 40, 1], [49, 46, 1], [49, 60, 1], [49, 73, 1], [49, 78, 1], [50, 16, 1], [50, 19, 1], [50, 28, 1], [50, 36, 1], [50, 64, 1], [50, 68, 1], [50, 70, 1], [50, 72, 1], [50, 77, 1], [50, 89, 1], [50, 99, 1], [51, 4, 1], [51, 5, 1], [51, 27, 1], [51, 29, 1], [51, 35, 1], [51, 39, 1], [51, 46, 1], [51, 59, 1], [51, 63, 1], [51, 72, 1], [51, 82, 1], [51, 88, 1], [51, 97, 1], [52, 9, 1], [52, 45, 1], [52, 72, 1], [52, 75, 1], [53, 0, 1], [53, 31, 1], [53, 36, 1], [53, 40, 1], [53, 45, 1], [53, 46, 1], [53, 55, 1], [53, 69, 1], [53, 76, 1], [53, 85, 1], [53, 94, 1], [54, 22, 1], [54, 24, 1], [54, 33, 1], [54, 61, 1], [54, 86, 1], [55, 3, 1], [55, 23, 1], [55, 32, 1], [55, 36, 1], [55, 37, 1], [55, 48, 1], [55, 53, 1], [55, 61, 1], [55, 67, 1], [55, 94, 1], [56, 20, 1], [56, 34, 1], [56, 43, 1], [56, 47, 1], [56, 60, 1], [56, 61, 1], [56, 68, 1], [56, 70, 1], [56, 73, 1], [56, 86, 1], [57, 13, 1], [57, 29, 1], [57, 30, 1], [57, 40, 1], [57, 42, 1], [57, 46, 1], [57, 58, 1], [57, 61, 1], [57, 71, 1], [57, 78, 1], [57, 81, 1], [57, 89, 1], [57, 91, 1], [57, 95, 1], [58, 11, 1], [58, 39, 1], [58, 47, 1], [58, 57, 1], [58, 62, 1], [58, 68, 1], [58, 75, 1], [58, 91, 1], [58, 96, 1], [58, 98, 1], [59, 16, 1], [59, 32, 1], [59, 51, 1], [59, 61, 1], [59, 65, 1], [60, 2, 1], [60, 4, 1], [60, 5, 1], [60, 6, 1], [60, 13, 1], [60, 30, 1], [60, 37, 1], [60, 38, 1], [60, 44, 1], [60, 49, 1], [60, 56, 1], [60, 79, 1], [60, 80, 1], [60, 83, 1], [61, 5, 1], [61, 6, 1], [61, 10, 1], [61, 12, 1], [61, 19, 1], [61, 36, 1], [61, 54, 1], [61, 55, 1], [61, 56, 1], [61, 57, 1], [61, 59, 1], [61, 68, 1], [61, 73, 1], [61, 78, 1], [61, 81, 1], [62, 3, 1], [62, 8, 1], [62, 21, 1], [62, 24, 1], [62, 25, 1], [62, 36, 1], [62, 37, 1], [62, 58, 1], [62, 66, 1], [62, 80, 1], [62, 85, 1], [62, 87, 1], [63, 11, 1], [63, 13, 1], [63, 19, 1], [63, 20, 1], [63, 27, 1], [63, 34, 1], [63, 40, 1], [63, 43, 1], [63, 51, 1], [63, 67, 1], [63, 83, 1], [64, 9, 1], [64, 22, 1], [64, 50, 1], [64, 68, 1], [64, 76, 1], [64, 80, 1], [65, 1, 1], [65, 4, 1], [65, 16, 1], [65, 30, 1], [65, 43, 1], [65, 59, 1], [65, 73, 1], [65, 95, 1], [65, 97, 1], [66, 6, 1], [66, 8, 1], [66, 18, 1], [66, 20, 1], [66, 22, 1], [66, 23, 1], [66, 31, 1], [66, 46, 1], [66, 62, 1], [66, 73, 1], [66, 76, 1], [66, 90, 1], [66, 92, 1], [67, 2, 1], [67, 16, 1], [67, 29, 1], [67, 45, 1], [67, 55, 1], [67, 63, 1], [67, 80, 1], [67, 83, 1], [67, 84, 1], [67, 89, 1], [68, 9, 1], [68, 12, 1], [68, 18, 1], [68, 50, 1], [68, 56, 1], [68, 58, 1], [68, 61, 1], [68, 64, 1], [68, 70, 1], [68, 96, 1], [68, 97, 1], [69, 1, 1], [69, 11, 1], [69, 26, 1], [69, 53, 1], [69, 75, 1], [69, 77, 1], [69, 84, 1], [70, 8, 1], [70, 11, 1], [70, 18, 1], [70, 39, 1], [70, 50, 1], [70, 56, 1], [70, 68, 1], [70, 80, 1], [70, 86, 1], [70, 88, 1], [70, 93, 1], [71, 22, 1], [71, 37, 1], [71, 57, 1], [71, 81, 1], [71, 90, 1], [72, 2, 1], [72, 4, 1], [72, 6, 1], [72, 8, 1], [72, 28, 1], [72, 32, 1], [72, 50, 1], [72, 51, 1], [72, 52, 1], [72, 98, 1], [73, 26, 1], [73, 45, 1], [73, 46, 1], [73, 49, 1], [73, 56, 1], [73, 61, 1], [73, 65, 1], [73, 66, 1], [74, 7, 1], [74, 11, 1], [74, 13, 1], [74, 18, 1], [74, 20, 1], [74, 41, 1], [74, 75, 1], [74, 84, 1], [74, 90, 1], [75, 8, 1], [75, 24, 1], [75, 35, 1], [75, 40, 1], [75, 42, 1], [75, 43, 1], [75, 44, 1], [75, 45, 1], [75, 52, 1], [75, 58, 1], [75, 69, 1], [75, 74, 1], [75, 96, 1], [76, 1, 1], [76, 10, 1], [76, 15, 1], [76, 39, 1], [76, 42, 1], [76, 48, 1], [76, 53, 1], [76, 64, 1], [76, 66, 1], [76, 86, 1], [77, 3, 1], [77, 6, 1], [77, 33, 1], [77, 36, 1], [77, 43, 1], [77, 50, 1], [77, 69, 1], [77, 84, 1], [77, 89, 1], [78, 6, 1], [78, 11, 1], [78, 28, 1], [78, 38, 1], [78, 44, 1], [78, 46, 1], [78, 49, 1], [78, 57, 1], [78, 61, 1], [78, 91, 1], [78, 94, 1], [79, 3, 1], [79, 39, 1], [79, 60, 1], [80, 19, 1], [80, 27, 1], [80, 36, 1], [80, 46, 1], [80, 60, 1], [80, 62, 1], [80, 64, 1], [80, 67, 1], [80, 70, 1], [80, 85, 1], [80, 91, 1], [81, 4, 1], [81, 5, 1], [81, 23, 1], [81, 34, 1], [81, 45, 1], [81, 57, 1], [81, 61, 1], [81, 71, 1], [81, 87, 1], [81, 97, 1], [82, 1, 1], [82, 2, 1], [82, 3, 1], [82, 4, 1], [82, 13, 1], [82, 37, 1], [82, 42, 1], [82, 51, 1], [82, 83, 1], [82, 84, 1], [82, 96, 1], [83, 1, 1], [83, 3, 1], [83, 12, 1], [83, 17, 1], [83, 33, 1], [83, 34, 1], [83, 44, 1], [83, 46, 1], [83, 60, 1], [83, 63, 1], [83, 67, 1], [83, 82, 1], [83, 89, 1], [83, 93, 1], [83, 98, 1], [84, 17, 1], [84, 26, 1], [84, 67, 1], [84, 69, 1], [84, 74, 1], [84, 77, 1], [84, 82, 1], [84, 90, 1], [84, 92, 1], [85, 1, 1], [85, 6, 1], [85, 7, 1], [85, 9, 1], [85, 10, 1], [85, 18, 1], [85, 33, 1], [85, 37, 1], [85, 44, 1], [85, 53, 1], [85, 62, 1], [85, 80, 1], [85, 87, 1], [85, 95, 1], [86, 2, 1], [86, 3, 1], [86, 5, 1], [86, 10, 1], [86, 33, 1], [86, 39, 1], [86, 54, 1], [86, 56, 1], [86, 70, 1], [86, 76, 1], [87, 2, 1], [87, 4, 1], [87, 11, 1], [87, 33, 1], [87, 42, 1], [87, 62, 1], [87, 81, 1], [87, 85, 1], [87, 94, 1], [88, 2, 1], [88, 22, 1], [88, 28, 1], [88, 40, 1], [88, 46, 1], [88, 51, 1], [88, 70, 1], [88, 91, 1], [88, 92, 1], [88, 94, 1], [89, 5, 1], [89, 24, 1], [89, 37, 1], [89, 50, 1], [89, 57, 1], [89, 67, 1], [89, 77, 1], [89, 83, 1], [89, 95, 1], [90, 0, 1], [90, 12, 1], [90, 17, 1], [90, 25, 1], [90, 34, 1], [90, 66, 1], [90, 71, 1], [90, 74, 1], [90, 84, 1], [90, 97, 1], [91, 17, 1], [91, 18, 1], [91, 28, 1], [91, 31, 1], [91, 45, 1], [91, 47, 1], [91, 48, 1], [91, 57, 1], [91, 58, 1], [91, 78, 1], [91, 80, 1], [91, 88, 1], [91, 99, 1], [92, 3, 1], [92, 6, 1], [92, 8, 1], [92, 9, 1], [92, 18, 1], [92, 23, 1], [92, 29, 1], [92, 32, 1], [92, 47, 1], [92, 66, 1], [92, 84, 1], [92, 88, 1], [92, 99, 1], [93, 19, 1], [93, 47, 1], [93, 70, 1], [93, 83, 1], [94, 3, 1], [94, 7, 1], [94, 8, 1], [94, 9, 1], [94, 16, 1], [94, 27, 1], [94, 53, 1], [94, 55, 1], [94, 78, 1], [94, 87, 1], [94, 88, 1], [94, 97, 1], [95, 16, 1], [95, 31, 1], [95, 37, 1], [95, 43, 1], [95, 57, 1], [95, 65, 1], [95, 85, 1], [95, 89, 1], [95, 97, 1], [96, 10, 1], [96, 11, 1], [96, 21, 1], [96, 24, 1], [96, 27, 1], [96, 34, 1], [96, 58, 1], [96, 68, 1], [96, 75, 1], [96, 82, 1], [96, 98, 1], [97, 1, 1], [97, 8, 1], [97, 29, 1], [97, 51, 1], [97, 65, 1], [97, 68, 1], [97, 81, 1], [97, 90, 1], [97, 94, 1], [97, 95, 1], [98, 2, 1], [98, 3, 1], [98, 27, 1], [98, 36, 1], [98, 48, 1], [98, 58, 1], [98, 72, 1], [98, 83, 1], [98, 96, 1], [98, 99, 1], [99, 5, 1], [99, 22, 1], [99, 28, 1], [99, 47, 1], [99, 48, 1], [99, 50, 1], [99, 91, 1], [99, 92, 1], [99, 98, 1]]

matrix_raw = np.zeros((100, 100))
# Loop through the list of tuples and set corresponding positions to 1
for pos in lst:
    row = pos[0]
    col = pos[1]
    val = pos[2]
    matrix_raw[row][col] = val

graph = matrix_raw

# Define the number of nodes
num_nodes = 100

# Define the initial solution as a random partition of the nodes
# random.randint(0, 1) Generates either 0 or 1, with equal probability 
#basically, this is randomly generating a solution to see if it works
#solution corresponds to randomly breaking the entire set into two sets and assigning each vertex a value of 0 or 1
solution = [random.randint(0, 1) for i in range(num_nodes)]
print('this is initial, random solution', solution)

# Define the objective function to maximize (i.e., the size of the cut)
#In this Python snippet, the clause `solution[i] != solution[j]` is used to check if two nodes `i` and `j` 
#belong to different groups in the given solution. 
#The `objective_function` takes a solution as input, which is a list of binary values (0 or 1) 
#indicating the group membership of each node in a graph. 
#The function computes the size of the cut between the two groups by iterating 
#over all pairs of nodes and counting the number of edges that cross between the groups. 
#The clause `graph[i][j] == 1` checks if there is an edge between nodes 
#`i` and `j` in the graph. If there is an edge, and if `solution[i] != solution[j]`, 
#then the edge crosses between the two groups and contributes to the cut size. 
#If `solution[i] == solution[j]`, then the edge is within the same group and does not contribute to the cut size.
#In other words, the clause `solution[i] != solution[j]` is used to identify 
#edges that cross between different groups and contribute to the cut size.
def objective_function(solution):
    cut_size = 0
    for i in range(num_nodes):
        for j in range(num_nodes):
            if graph[i][j] == 1 and solution[i] != solution[j]:
                cut_size += 1
                #print('this is cut_size', cut_size)
    return cut_size


# Define the ground state function to minimize (i.e., the total negative energy)
def ground_state_function(solution):
    energy = 0
    for i in range(num_nodes):
        for j in range(num_nodes):
            if graph[i][j] == 1:
                energy -= (2 * solution[i] - 1) * (2 * solution[j] - 1)
    return energy

#cut and pasted this method from below; separate solution; do not use
def max_cut(graph):
    n = len(graph)
    best_cut = -1
    best_partition = None
    for partition in itertools.product([0, 1], repeat=n):
        cut = 0
        for i in range(n):
            for j in range(i+1, n):
                if graph[i][j] and partition[i] != partition[j]:
                    cut += 1
        if cut > best_cut:
            best_cut = cut
            best_partition = partition
            #print('this is cut', cut)
            #print('this is partition', partition)
    return best_cut, best_partition

# Define the temperature schedule
def temperature_schedule(initial_temperature, cooling_rate):
    temperature = initial_temperature
    while True:
        yield temperature
        temperature *= cooling_rate
        
        

# Define the acceptance probability function
def acceptance_probability(delta, temperature):
    return math.exp(delta / temperature)

# Set the initial temperature and cooling rate
initial_temperature = 150000
cooling_rate = 0.9999

# Initialize the best solution and its objective function value
best_solution = solution.copy()
best_value = objective_function(solution)
best_ground_state = ground_state_function(solution)


# Initialize the current solution and its objective function value
current_solution = solution.copy()
current_value = best_value
current_ground_state = best_ground_state


# Initialize the iteration counter
iteration = 0

# Initialize the temperature generator
temperature_gen = temperature_schedule(initial_temperature, cooling_rate)

# Loop until the stopping criterion is met (e.g., maximum number of iterations)
while iteration < 150000:
    # Select a random neighbor of the current solution by flipping one node
    neighbor = current_solution.copy()
    index = random.randint(0, num_nodes-1)
    #this appears to randomly choose an index in the solution set
    neighbor[index] = 1 - neighbor[index]
    #this flips the random index in solution set from 0 to 1, or a 1 to 0

    # Evaluate the objective function of the neighbor
    neighbor_value = objective_function(neighbor)
    neighbor_ground_state = ground_state_function(neighbor)

    # Calculate the delta of the objective function between the current and neighbor solutions
    delta = neighbor_value - current_value

    # If the neighbor solution is better than the current solution, accept it as the new current solution
    if delta > 0:
        current_solution = neighbor.copy()
        current_value = neighbor_value
        #print('this is positive delta', delta)
    # If the neighbor solution is worse than the current solution, accept it with a certain probability based on the temperature
        current_ground_state = neighbor_ground_state
    else:
        temperature = next(temperature_gen)
        ap = acceptance_probability(delta, temperature)
        #print('this is delta', delta)
        #print('this is ap', ap)
        #In Python, random.random() generates a random float number between 0 and 1 (excluding 1).
        #ap shrinks over time, so less chance that random.random() will be lower than ap
        if random.random() < ap:
            current_solution = neighbor.copy()
            current_value = neighbor_value
            current_ground_state = neighbor_ground_state

    # If the current solution is better than the best solution found so far, update the best solution and its objective function value
    if current_value > best_value:
        best_solution = current_solution.copy()
        best_value = current_value
        best_ground_state = current_ground_state


    # Increment the iteration counter
    iteration += 1

# Print the best solution and its objective function value
print("Best solution:", best_solution)
print("Objective function value:", best_value)
print("Ground state energy:", best_ground_state)

