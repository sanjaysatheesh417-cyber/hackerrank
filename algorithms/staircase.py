#problem 4
#https://www.hackerrank.com/challenges/staircase
def staircase(n):
    # Write your code here
    for i in range(n):
        if i!=(n-1):
            print(" "*(n-(i+2)),"#"*(i+1))
        else:
            print("#"*(n))
