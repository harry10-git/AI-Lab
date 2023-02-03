# BST and travsersal

class Node:
    def __init__(self,item):
        self.item= item
        self.left = None
        self.right = None

def insert(node,item):

        if node is None:
            return Node(item)

        elif item < node.item :
            node.left = insert(node.left, item)

        elif item > node.item :
            node.right = insert(node.right, item)

        return node


def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.item, end=" ")
        inorder(node.right)


def preorder(node):
    if node is not None:
        print(node.item, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.item, end=" ")






root = None
root = insert(root, 5)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 9)
root = insert(root, 8)
root = insert(root, 2)

print("In-order")
inorder(root)

print("\nPre-order")
preorder(root)

print("\nPost-order")
postorder(root)