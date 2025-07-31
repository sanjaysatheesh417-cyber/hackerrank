#PROBLEM 3
#https://www.hackerrank.com/challenges/plus-minus
def plusminus(arr):
    # Write your code here
    plus=0
    minus=0
    zero=0
    for i in arr:
        if i>0:
            plus+=1
        elif i<0:
            minus+=1
        elif i==0:
            zero+=1
    res=[plus,minus,zero]
    for i in res:
        print(f"{(i/len(arr)):.6f}")