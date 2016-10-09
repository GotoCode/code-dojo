'''
    problem statement
    
    Implement insert and delete operations for 
    a doubly-linked list
'''


# a single node (in a doubly-linked list)

class Node(object):
    
    def __init__(self, value, prev=None, next=None):
    
        self.value = value
        self.prev  = prev
        self.next  = next


# a doubly-linked list object

class DLL(object):
    
    def __init__(self, head=None):
        self.head = head


def insert(ll, newValue):

    if ll == None:
        return
        
    elif ll.head == None:
        ll.head = Node(newValue, None, None)
        
    else:
    
        newNode = Node(newValue)
        
        currNode = ll.head
        
        while currNode != None:
        
            if currNode.next == None:
            
                newNode.prev  = currNode
                currNode.next = newNode
                break
        
            currNode = currNode.next


def delete(ll, delValue):
    
    if ll == None:
        return
        
    elif ll.head == None:
        return
    
    elif ll.head.value == delValue:
        
        ll.head = ll.head.next
        
        if ll.head != None:
            ll.head.prev = None
        
    else:
        currNode = ll.head
        
        while currNode != None:
            
            if currNode.next != None and currNode.next.value == delValue:
                
                # adjust forward pointer to 'skip over' deleted node
                currNode.next = currNode.next.next
                
                # adjust backward pointer to 'skip over' deleted node
                if currNode.next != None:
                    currNode.next.prev = currNode
                
                break
            
            currNode = currNode.next


# test cases #

if __name__ == '__main__':

    testList1 = DLL()

    insert(testList1, 1)
    assert testList1.head.value == 1
    
    insert(testList1, 2)
    assert testList1.head.next.value == 2
    assert testList1.head.next.prev.value == 1

    insert(testList1, 3)
    assert testList1.head.next.next.value == 3

    delete(testList1, 4)
    assert testList1.head.value == 1
    assert testList1.head.next.value == 2
    assert testList1.head.next.next.value == 3

    delete(testList1, 2)
    assert testList1.head.value == 1
    assert testList1.head.next.value == 3
    
    delete(testList1, 3)
    assert testList1.head.value == 1
    assert testList1.head.next == None
    
    delete(testList1, 1)
    assert testList1 != None
    assert testList1.head == None
    
    print 'All tests complete!'
