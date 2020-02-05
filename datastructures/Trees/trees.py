

class Node:

    def __init__(self,key):
        self.root = key
        self.left = None
        self.right = None

    
#We create the instance of the class
val = Node(1)

# So to the left side of the root you are creating another node
val.left = Node(2)

# So to the right side of the root you are creating another node
val.right = Node(3)

# Here if we want to stop no need to create the node else we can create the node
val.left.left = 4

print(val.left.left)

