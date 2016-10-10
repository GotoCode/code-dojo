'''
    problem statement
    
    Given an array of integers from 1 to 1000000,
    find that element which occurs exactly twice
'''


def findDup(nums):

    counts = {}
    
    for n in nums:
        
        counts[n] = counts.get(n, 0) + 1
        
        if counts[n] > 1:
            return n
    
    return None


def findDup2(nums):
    
    nums.sort()
    
    for i in xrange(len(nums)-1):
        
        if nums[i] == nums[i+1]:
            return nums[i]
    
    return None

