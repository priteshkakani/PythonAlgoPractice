
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def preorder_traversal(root):
    if(root):
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if(root):
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

def postorder_traversal(root):
    if(root):

        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.left = Node(5)

print "Preorder Traversal of tree is"
preorder_traversal(root)

print "Inorder Traversal of tree is"
inorder_traversal(root)

print "Postorder Traversal of tree is"
postorder_traversal(root)


