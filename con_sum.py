'''
    problem statement
    
    Given an array of integers,
    return the largest sum of 
    contiguous integers in 
    the array
'''


def maxSumFrom(nums, start):
    
    maxSum  = 0
    currSum = 0
    
    for i in xrange(start, len(nums)):
        
        currSum += nums[i]
        
        if currSum > maxSum:
            maxSum = currSum
    
    return maxSum


def maxContigSum(nums):
    
    if len(nums) == 0:
        
        return 0
        
    else:
        
        maxValue = 0
        
        for start in xrange(len(nums)):
            
            currValue = maxSumFrom(nums, start)
            
            if currValue > maxValue:
                maxValue = currValue
        
        return maxValue
        
