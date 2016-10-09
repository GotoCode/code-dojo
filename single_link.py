'''
    problem statement
    
    Implement insert & delete operations 
    for a singly-linked list
    
    Lessons Learned
    
        ~ when given arg of type obj, we have
          a 'pointer' that points to the object
          in memory
          
        ~ 'self' is also a pointer to the in-memory
           object
'''


class Node(object):
    
    def __init__(self, value, next=None):
        self.value = value
        self.next  = next
    
    def pushOver(self):
        
        self = self.next


def insert(ll, newValue):
    
    if ll == None:
        return Node(newValue)
        
    else:
        currNode = ll
        
        while currNode.next != None:
            currNode = currNode.next
        
        currNode.next = Node(newValue)
        
        return ll


def delete(ll, delValue):
    
    if ll == None:
        return ll
    elif ll.value == delValue:
        ll = ll.next
        return ll
    else:
        currNode = ll
        
        while currNode != None:
            
            if currNode.next != None and currNode.next.value == delValue:
                currNode.next = currNode.next.next
                return ll
                
            currNode = currNode.next
        
        return ll

