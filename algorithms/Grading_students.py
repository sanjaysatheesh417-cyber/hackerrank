#problem 7
#https://www.hackerrank.com/challenges/grading
def gradingStudents(grades):
    # Write your code here
    res=[]
    for i in grades:
        if (i%5) >= 3 and i>=38:
            res.append(i+(5-(i%5)))
        else:
            res.append(i)
    return res
