'''
    problem statement
    
    Given a linked list,
    find the middle element
'''

# a single node in a singly-linked list

class Node(object):

    def __init__(self, value, next=None):
        
        self.value = value
        self.next  = next


# a singly-linked list object

class LL(object):

    def __init__(self, head=None):
        
        self.head = head
    
    def getLen(self):
        
        length = 0
        
        currNode = self.head 
        
        while currNode != None:
            length += 1
            currNode = currNode.next
        
        return length


# input  - ll : LL (no cycles)
# output - midNode : Node

def findMid(ll):
    
    if ll == None:
    
        return None
   
    else:
    
        slow = ll.head
        fast = ll.head
        
        while fast != None and slow != None:
            
            if fast.next == None or fast.next.next == None:
               break
            
            fast = fast.next.next
            slow = slow.next
        
        return slow

#        v
# [1, 2, 3, 4]
#     ^
