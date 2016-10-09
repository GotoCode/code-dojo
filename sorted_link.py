'''
    problem statement
    
    Implement insert and delete for 
    sorted (singly-)linked list
'''


# a single node in a linked list

class Node(object):

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    
# a singly-linked list object

class LL(object):
    
    def __init__(self, head=None):
        self.head = head
    

# REQUIRES: ll is SORTED in ascending order
# ENSURES:  ll is SORTED after inserting newValue

def insert(ll, newValue):
    
    if ll == None:
        return
        
    elif ll.head == None:
        ll.head = Node(newValue)
    
    elif newValue <= ll.head.value:
    
        newNode = Node(newValue, ll.head)
        ll.head = newNode
        
    else:
        currNode = ll.head
        
        while currNode != None:
        
            if currNode.next != None and newValue <= currNode.next.value:
            
                newNode = Node(newValue, currNode.next)
                currNode.next = newNode
                break
            
            elif currNode.next == None:
                
                currNode.next = Node(newValue)
                break
            
            currNode = currNode.next


# REQUIRES: ll is SORTED in ascending order
# ENSURES:  ll is SORTED after deleted delValue

def delete(ll, delValue):
    
    if ll == None:
        return
        
    elif ll.head == None:
        return
        
    elif ll.head.value == delValue:
        ll.head = ll.head.next
        
    else:
        currNode = ll.head
        
        while currNode != None:
            
            if currNode.next != None:
                
                nextValue = currNode.next.value
                
                if nextValue == delValue:
                    currNode.next = currNode.next.next
                    break
                elif nextValue > delValue:
                    break

            currNode = currNode.next


# test cases #

if __name__ == '__main__':
    
    testList1 = LL()

    insert(testList1, 1)
    assert testList1.head.value == 1
    
    insert(testList1, 3)
    assert testList1.head.next.value == 3

    insert(testList1, 5)
    assert testList1.head.next.next.value == 5

    delete(testList1, 1)
    assert testList1.head.value == 3
    assert testList1.head.next.value == 5

    delete(testList1, 4)
    assert testList1.head.value == 3
    assert testList1.head.next.value == 5
    
    delete(testList1, 5)
    assert testList1.head.value == 3
    assert testList1.head.next == None
    
    print 'All tests complete!'