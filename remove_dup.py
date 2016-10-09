'''
    problem statement
    
    Given an input string, remove any duplicate chars
'''


def removeDup(s):
    
    newStr = ''
    
    seen = {}
    
    for ch in s:
        
        if not seen.get(ch, False):
        
            newStr += ch
            seen[ch] = True
    
    return newStr

