'''
    problem statement
    
    Given an array of elements,
    implement a (linear-time)
    shuffle function
'''

import random


def swap(arr, i, j):
    
    temp   = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def shuffle(arr):
    
    for i in xrange(len(arr)):
        
        swap(arr, i, random.randint(0, len(arr)-1))
    
    return arr

