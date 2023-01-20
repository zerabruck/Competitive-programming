#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    index = -1
    value = arr[-1]
    for i in range(n - 2,-1,-1):
        if value < arr[i] and i != 0:
            arr[index] = arr[i]
            index = i
            string = ' '.join([ str(val) for val in arr])
            print(string)
            
            
        elif value >= arr[i]:
            arr[index] = value
            string = ' '.join([ str(val) for val in arr])
            print(string)
            break
        if i == 0 and value < arr[i] :
            arr[1] = arr[0]
            string = ' '.join([ str(val) for val in arr])
            print(string)
            
            arr[0] = value
            
            string = ' '.join([ str(val) for val in arr])
            print(string)
            
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
