'''
Given a 6X6 2D Array:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass is a subset of values with indices falling in this pattern as a graphical representation:
a b c
  d
e f g
An hourglass sum is the sum of an hourglass' values. 
Calculate the hourglass sum for every hourglass in the array, then print the maximum hourglass sum. 
The array will always be 6X6
'''

#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    x = 6
    y = 6 #can convert to numpy array and use numpy.shape()
    result_arr = []
    for i in range(0,4):
        for j in range(0,4):
            sum = 0
            for k in range(j,j+3):
                sum += arr[i][k] + arr[i+2][k]
            sum += arr[i+1][math.floor((j+j+3)/2)]
            result_arr.append(sum)
    
    print(result_arr)
    result_arr.sort()
    return result_arr[-1]            
        
    pass
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
