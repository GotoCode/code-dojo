'''
    problem statement
    
    Split a linked list given a pivot value
'''


# a single node in a singly-linked list
class Node(object):
    
    def __init__(self, value, next=None):
    
        self.value = value
        self.next  = next


# a singly-linked list object
class LL(object):
    
    def __init__(self):
    
        self.head = None
        self.tail = None
    
    def insert(self, newNode):
        
        if self.head == None:
        
            self.head = newNode
            self.tail = self.head
        
        else:
        
            self.tail.next = newNode
            self.tail = newNode
    
    def __str__(self):
        
        nodeValues = []
        
        currNode = self.head
        
        while currNode != None:
            
            nodeValues.append(currNode.value)
            
            currNode = currNode.next
        
        return ' -> '.join(map(str, nodeValues))



# input - ll    : linked list 
#         pivot : val

# output - lt    : linked list (items <= pivot)
#          gt    : linked list (items > pivot)

def split(ll, pivot):
    
    if ll == None:
        return None
        
    elif ll.head == None:
    
        lt = LL()
        gt = LL()
        
        return (lt, gt)

    else:
        
        currNode = ll.head
        
        lt = LL()
        gt = LL()
        
        while currNode != None:
        
            nextNode = currNode.next
            
            currNode.next = None
            
            if currNode.value <= pivot:
                lt.insert(currNode)
            else:
                gt.insert(currNode)
            
            currNode = nextNode
        
        # the old list is now destroyed...
        ll.head = None
        
        return (lt, gt)

