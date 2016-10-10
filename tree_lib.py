'''
    problem statement
    
    Given a binary (search) tree, implement
    insert operation and preorder, inorder, 
    and postorder traversals
    
    LESSON OF THE DAY
    
      ~ DFS can be recursive OR non-recursive
      ~ for recursive functions, use "wrapper/helper" pattern
'''


# a single node in a BST

class Node(object):
    
    def __init__(self, value, left=None, right=None):
        
        self.value = value
        self.left  = left
        self.right = right


# a binary search tree object (cannot contain repeats)

class BST(object):
    

    def __init__(self, root=None):
        
        self.root = root


    def insert(self, newValue):
        
        if self.root == None:
        
            self.root = Node(newValue)
        
        else:
        
            currNode = self.root
            
            while currNode != None:
                
                if newValue < currNode.value:
                    
                    if currNode.left == None:
                        currNode.left = Node(newValue)
                        return
                    else:
                        currNode = currNode.left
                    
                elif newValue > currNode.value:
                    
                    if currNode.right == None:
                        currNode.right = Node(newValue)
                        return
                    else:
                        currNode = currNode.right
                    
                else:
                    return

    def printInOrder(self):
    
        self.printInOrderHelper(self.root)
    
    def printInOrderHelper(self, start):
        
        if start != None:
        
            self.printInOrderHelper(start.left)
                
            print start.value,
                
            self.printInOrderHelper(start.right)
    
    def printPreOrder(self):
    
        self.printPreOrderHelper(self.root)
    
    def printPreOrderHelper(self, start):
        
        if start != None:
            
            print start.value,
            
            self.printPreOrderHelper(start.left)
            
            self.printPreOrderHelper(start.right)
    
    def printPostOrder(self):
    
        self.printPostOrderHelper(self.root)
    
    def printPostOrderHelper(self, start):
        
        if start != None:
            
            self.printPostOrderHelper(start.left)
            
            self.printPostOrderHelper(start.right)
            
            print start.value,
    
    