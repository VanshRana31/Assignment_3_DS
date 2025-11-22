class Node:
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location
        self.left = None
        self.right = None
        self.height = 1

# ------------------ BST INSERT ------------------
def insert_bst(root, node):
    if root is None:
        return node
    if node.id < root.id:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
    return root

# ------------------ TRAVERSALS ------------------
def inorder(root):
    return inorder(root.left) + [(root.id, root.name)] + inorder(root.right) if root else []

def preorder(root):
    return [(root.id, root.name)] + preorder(root.left) + preorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [(root.id, root.name)] if root else []

# ------------------ AVL FUNCTIONS ------------------
def height(n):
    return n.height if n else 0

def get_balance(n):
    return height(n.left) - height(n.right) if n else 0

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    y.height = max(height(y.left), height(y.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    x.height = max(height(x.left), height(x.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y

def insert_avl(root, node):
    if root is None:
        return node
    if node.id < root.id:
        root.left = insert_avl(root.left, node)
    else:
        root.right = insert_avl(root.right, node)

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    # LL
    if balance > 1 and node.id < root.left.id:
        return right_rotate(root)
    # RR
    if balance < -1 and node.id > root.right.id:
        return left_rotate(root)
    # LR
    if balance > 1 and node.id > root.left.id:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # RL
    if balance < -1 and node.id < root.right.id:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root
