'''
    problem statement
    
    Given a BST, implement an non-recursive
    inorder function
    
    LESSON OF THE DAY
      
      ~ use iterative examples
'''


# a single node in a BST

class Node(object):
    
    def __init__(self, value, left=None, right=None):
        
        self.value = value
        self.left  = left
        self.right = right


# a binary search tree object

class BST(object):
    

    def __init__(self, root=None):
        
        self.root = root


    def inorder(self):
        
        if self.root == None:
        
            return
        
        else:
            
            nextStack = [self.root]
            
            while len(nextStack) > 0:
                
                currNode = nextStack.pop()
                
                if len(nextStack) > 0 and nextStack[-1] == currNode.right:
                    print currNode.value, 
                    continue
                
                if currNode.right:
                    nextStack.append(currNode.right)
                
                if currNode.left:
                    nextStack.append(currNode)
                    nextStack.append(currNode.left)
                else:
                    print currNode.value, 
    
    

