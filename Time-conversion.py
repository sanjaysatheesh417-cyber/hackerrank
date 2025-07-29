#Problem 6
#https://www.hackerrank.com/challenges/time-conversion
def timeConversion(s):
    # Write your code here
    res=""
    if (s[:2] == "12" and s[8:] == "PM") or ((s[:2] != "12") and (s[8:] == "AM")):
        res += s[:8]
    elif (s[:2] == "12") and (s[8:] == "AM"):
        res += ("00"+s[2:8])
    else:
        res += ((str(int(s[:2])+12))+s[2:8])
    return res
