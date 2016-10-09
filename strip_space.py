'''
    problem statement
    
    Given an input string, strip leading 
    (and trailing) whitespace chars
    
    (whitespace == '\t', ' ', '\n', '\r')
'''


def findStart(s):
    
    start = 0
    
    while start < len(s) and s[start].isspace():
        start += 1
    
    return start
    

def findEnd(s):
    
    end = len(s) - 1
    
    while end >= 0 and s[end].isspace():
        end -= 1
    
    return end


def stripSpaces(s):
    
    return s[findStart(s) : findEnd(s) + 1]

