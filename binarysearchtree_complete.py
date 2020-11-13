def search(root,key):
     
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Key is smaller than root's key
    return search(root.left,key)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# A utility function to insert 
# a new node with the given key
 
 
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
r = Node(50)
r = insert(r, 30)
r = insert(r, 70)
r = insert(r, 40)
r = insert(r, 90)
def traverse(node):
    if node != None:
        traverse(node.left)
        print(node.val)
        traverse(node.right)
    
        
traverse(r)
    