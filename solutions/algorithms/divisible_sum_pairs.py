import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    # Write your code here
    res=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                if ar[i]<ar[j] and (ar[i]+ar[j])%k==0:
                    res+=1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
