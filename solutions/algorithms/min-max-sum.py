#problem 5
#https://www.hackerrank.com/challenges/mini-max-sum
def minimaxSum(arr):
    # Write your code here
    num=[]
    for i in arr:
        l=[]
        for j in arr:
            l.append(j)
        num.append(sum(l)-i)
    print(min(num),max(num))
