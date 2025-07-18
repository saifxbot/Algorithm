from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree():
    val = input("Enter root node value (or 'exit' to cancel): ") 
    if val.lower() == "exit" or val == "":
        return None
    root = Node(val)
    queue = [root]

    while queue:
        current = queue.pop(0)

        left_val = input(f"Enter LEFT child of {current.value} (or 'exit' to stop): ")
        if left_val.lower() == "exit":
            break
        elif left_val:
            current.left = Node(left_val)
            queue.append(current.left)

        right_val = input(f"Enter RIGHT child of {current.value} (or 'exit' to stop): ")
        if right_val.lower() == "exit":
            break
        elif right_val:
            current.right = Node(right_val)
            queue.append(current.right)

    return root

def print_tree_top_down(root, space=0, LEVEL_SPACE=5):
    if root is None:
        return

    space += LEVEL_SPACE
    print_tree_top_down(root.right, space)
    print()
    print(" " * (space - LEVEL_SPACE) + str(root.value))
    print_tree_top_down(root.left, space)

def preorder_traversal(root):
    if root:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')

def level_order_traversal(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Main driver
tree_root = build_tree()

if tree_root:
    print("\n🌳 Tree structure (top to bottom):")
    print_tree_top_down(tree_root)

    print("\n📌 Preorder Traversal:")
    preorder_traversal(tree_root)
    print()

    print("\n📌 Inorder Traversal:")
    inorder_traversal(tree_root)
    print()

    print("\n📌 Postorder Traversal:")
    postorder_traversal(tree_root)
    print()

    print("\n📌 Level Order Traversal (BFS):")
    level_order_traversal(tree_root)
    print()
else:
    print("No tree was created.")
