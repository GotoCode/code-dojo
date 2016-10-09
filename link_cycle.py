#
# problem statement
#
# Given a linked list (possibly containing a cycle),
# return the label of the first node of the cycle
#


# a single node in a linked list

class Node(object):
    
    def __init__(self, value, next=None):
    
        self.value = value
        self.next  = next
    
    def insert(self, newNode):
        
        currNode = self
        
        while currNode.next != None:
            currNode = currNode.next
        
        currNode.next = newNode
    
    def last(self):
    
        curr_node = self
        
        while curr_node.next != None:
            curr_node = curr_node.next
        
        return curr_node


# does this linked list have a cycle?
def hasCycle(ll):
    
    if ll == None:
    
        return False
    
    else:
    
        first  = ll
        second = first.next
        
        while second != None and second.next != None:
            
            # if the linked list is circular, second will eventually 'see' first
            if second == first or second.next == first:
                return True
            
            first  = first.next
            second = second.next.next
        
        # if second 'fell off the end' of the list, then it doesn't have a cycle
        return False


# splits the given ll at index n + 1 (assume: n >= 0)

#     v
# [1, 2, 3] 0 ==> [1, 2] [3]
#  ^

def splitList(ll, n):
    
    curr_node = ll
    end_fst   = curr_node
    
    if n == 0:
        return (None, curr_node)
    
    while n >= 0 and end_fst != None:
    
        if n == 0:
            second_part  = end_fst.next
            end_fst.next = None
            break
    
        end_fst = end_fst.next
        n = n - 1
    
    return (curr_node, second_part)


# solution function

def solution(ll):
    
    if ll == None:

        return ''

    else:
        
        # max distance to inspect
        max_dist = 0
        
        # first & second parts of truncated list
        first_part, second_part = splitList(ll, max_dist)
        
        # the most recent node we inspected
        latestNode = None
        
        while second_part != None:
        
            if hasCycle(first_part):
                return latestNode.value
                
            else:
                max_dist += 1
                
                if first_part != None:
                    latestNode = first_part.last()
                
                    first_part.insert(second_part)
                    first_part, second_part = splitList(first_part, max_dist)
                else:
                    first_part, second_part = splitList(ll, max_dist)
        
        return ''
                



# testing harness

if __name__ == '__main__':
    
    # create a cyclic linked list
    startNode1 = Node('A', Node('B', Node('C', Node('D'))))
    startNode1.next.next.next.next = startNode1
    
    testList1  = Node('0', startNode1)
    
    assert solution(testList1) == 'A'