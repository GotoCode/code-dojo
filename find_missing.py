'''
    problem statement
    
    Given an array of integers with values
    from 1 to 1000000, find the missing element
'''


def findMissing(nums):
    
    seen = {}
    
    # build up the dictionary of 'non-missing' items
    for n in nums:
        
        seen[n] = True
    
    # find which element is missing
    for i in xrange(1, 1000001):
        
        if not seen.get(i, False):
            return i
    
    return None


def findMissing2(nums):

    nums.sort()
    
    counter = 1
    
    for n in nums:
    
        if counter != n:
            return counter
    
        counter += 1

