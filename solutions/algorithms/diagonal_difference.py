#problem 2
#https://www.hackerrank.com/challenges/diagonal-difference
matrix = [[1,2,3],[4,5,6],[7,8,9]]
def diagonaldifference(arr):
    # Write your code here
    d1=0
    d2=0
    a=len(arr)
    for i in range(len(arr)):
        d1+=(arr[i][i])
        a-=1
        d2+=(arr[i][a])
    return abs(d1-d2)
result = diagonaldifference(matrix)
print("result:",result)