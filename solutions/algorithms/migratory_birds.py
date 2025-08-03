import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    # Write your code here
    res=[]
    counts=[]
    arr1=set(arr)
    for i in arr1:
        counts.append(arr.count(i))
    for j in arr:
        if arr.count(j) == max(counts):
            res.append(j)
    return min(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
