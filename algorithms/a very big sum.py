#problem 2
#https://www.hackerrank.com/challenges/diagonal-difference
def diagonalDifference(arr):
    # Write your code here
    d1=0
    d2=0
    a=len(arr)
    for i in range(len(arr)):
        d1+=(arr[i][i])
        a-=1
        d2+=(arr[i][a])
    return abs(d1-d2)