'''
    problem statement
    
    Given a string, return a reversed 
    version of the string
'''


def swap(arr, i, j):

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def revString(s):
    
    chars = [ch for ch in s]
    
    i = 0
    j = len(chars) - 1
    
    while i < j:
        
        swap(chars, i, j)
        
        i += 1
        j -= 1
    
    return ''.join(chars)

