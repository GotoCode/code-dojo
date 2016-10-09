'''
    problem statement
    
    Given an input string,
    find the first non-repeating char
'''


def findFirstUnique(s):
    
    if s == None:
    
        return None
    
    else:
        
        counts = {}
        
        # build up the counts dictionary
        for ch in s:
        
            counts[ch] = counts.get(ch, 0) + 1
        
        # find the first non-repeating (a.k.a. unique) char
        for ch in s:
            
            if counts[ch] == 1:
                return ch
        
        return None

