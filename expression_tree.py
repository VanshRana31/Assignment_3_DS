class ExpNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(expr):
    stack = []
    operators = []
    for ch in expr:
        if ch.isdigit():
            stack.append(ExpNode(ch))
        elif ch in "+-*/":
            operators.append(ch)
        elif ch == ")":
            op = operators.pop()
            right = stack.pop()
            left = stack.pop()
            node = ExpNode(op)
            node.left = left
            node.right = right
            stack.append(node)
    return stack[0]

def evaluate(root):
    if root.value.isdigit():
        return int(root.value)
    L = evaluate(root.left)
    R = evaluate(root.right)
    if root.value == "+": return L + R
    if root.value == "-": return L - R
    if root.value == "*": return L * R
    if root.value == "/": return L / R
