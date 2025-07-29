#problem 8
#https://www.hackerrank.com/challenges/apple-and-orange?isFullScreen=true
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    app=0
    orn=0
    for i in apples:
        if (i+a)>=s and (i+a)<=t:
            app+=1
    print(app)
    for j in oranges:
        if (j+b)>=s and (j+b)<=t:
            orn+=1
    print(orn)
