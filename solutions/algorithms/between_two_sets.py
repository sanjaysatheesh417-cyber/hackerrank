import math
import os
import random
import re
import sys

def getTotalX(a, b):
    # Write your code here
    res1=[]
    res2=[]
    for i in range(1,101):
        if all(i%n==0 for n in a):
            res1.append(i)
        if all(l%i==0 for l in b):
            res2.append(i)
    res=0
    for j in res1:
        if j in res2:
            res+=1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()