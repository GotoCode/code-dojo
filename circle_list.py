'''
    problem description
    
    Implement insert and delete operations
    for a circular (singly)-linked list
'''

# a single node in a singly-linked list

class Node(object):
    
    def __init__(self, value, next=None):
    
        self.value = value
        self.next  = next


# a circular (singly-)linked list object

class CircleList(object):
    
    def __init__(self, last=None):
    
        self.last = last



def insert(ll, newValue):

    if ll == None:
        return
    
    elif ll.last == None:
    
        newNode = Node(newValue)
        newNode.next = newNode
        
        ll.last = newNode
        
    else:
    
        newNode = Node(newValue)
        
        newNode.next = ll.last.next
        ll.last.next = newNode
        ll.last      = newNode



def delete(ll, delValue):

    if ll == None:
        return
        
    elif ll.last == None:
        return
    
    # the linked list contains only one element...
    elif ll.last.next == ll.last:
    
        if ll.last.value == delValue:
            ll.last = None
        else:
            return
    
    # the linked list contains more than one element...
    else:
        
        # start at the beginning of the circular linked list
        currNode = ll.last.next
        
        # we need to delete the 'head' node...
        if currNode.value == delValue:
        
            ll.last.next = currNode.next
        
        else:
        
            # stop once we've hit the end of the circle
            while currNode.next != ll.last.next:
            
                if currNode.next.value == delValue:
            
                    currNode.next = currNode.next.next
                    break
            
                currNode = currNode.next
    