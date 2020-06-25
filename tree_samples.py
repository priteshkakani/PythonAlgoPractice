
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#Time complexity O(n)
#Space complexity O(1)
def preorder_traversal(root):
    if(root):
        print(root.data)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

#Time complexity O(n)
#Space complexity O(1)
def inorder_traversal(root):
    if(root):
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

#Time complexity O(n)
#Space complexity O(1)
def postorder_traversal(root):
    if(root):
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data)

#Time complexity O(n2)
#Space complexity O(n)
def levelorder_traversal(root):
    h = height(root)
    for i in range(1,h+1):
        printGivenLevel(root,i)

#Time complexity O(n)
#Space complexity O(1)
def printGivenLevel(root, level):
    #print level
    if root is None:
        return
    if level == 1:
        print(root.data)
    elif level > 1 :
        printGivenLevel(root.left, level -1)
        printGivenLevel(root.right, level -1)


def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
    if rheight > lheight:
        return rheight+1
    else:
        return lheight+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.left = Node(5)

print "Pre order Traversal of tree is"
preorder_traversal(root)

print "In order Traversal of tree is"
inorder_traversal(root)

print "Post order Traversal of tree is"
postorder_traversal(root)

print "Level order Traversal of tree is"
levelorder_traversal(root)
