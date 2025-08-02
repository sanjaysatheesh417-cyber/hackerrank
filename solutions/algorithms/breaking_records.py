import math
import os
import random
import re
import sys

def breakingRecords(scores):
    # Write your code here
    n1=0
    n2=0
    high = scores[0]
    low = scores[0]
    for i in scores:
        if i>high:
            n1+=1
            high = i
        elif i<low:
            n2+=1
            low = i
    return [n1,n2]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
