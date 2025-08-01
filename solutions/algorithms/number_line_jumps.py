import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1==x2:
        if v1==v2:
            return "YES"
        else:
            return "NO"
    if v1<=v2 and x1<x2:
        return "NO"
    if ((x2-x1)%(v1-v2)) == 0 and (x2-x1)/(v1-v2) >= 0:
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
