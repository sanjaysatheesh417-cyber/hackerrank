def comparetriplets(a, b):
    # Write your code here
    l=[]
    for i in range(3):
        l.append([a[i],b[i]])
    r1=0
    r2=0
    for i in l:
        if i[0]>i[1]:
            r1+=1
        elif i[1]>i[0]:
            r2+=1
    return r1,r2