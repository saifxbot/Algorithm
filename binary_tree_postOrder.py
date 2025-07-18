class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree():
    val = input("📌 Enter root node value (or 'exit' to cancel): ") 
    if val.lower() == "exit" or val == "":
        return None

    root = Node(val)
    queue = [root]

    while queue:
        current = queue.pop(0)

        left_val = input(f"↪️ Enter LEFT child of {current.value} (or 'exit' to stop): ")
        if left_val.lower() == "exit":
            break
        elif left_val:
            current.left = Node(left_val)
            queue.append(current.left)

        right_val = input(f"↪️ Enter RIGHT child of {current.value} (or 'exit' to stop): ")
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

def postorder_traversal(root):
    if root is None:
        return []
    result = []
    result += postorder_traversal(root.left)
    result += postorder_traversal(root.right)
    result.append(root.value)
    return result

# Main driver
tree_root = build_tree()

if tree_root:
    print("\n🌳 Tree structure (top to bottom):")
    print_tree_top_down(tree_root)

    print("\n🔁 Postorder Traversal (Left → Right → Root):")
    postorder = postorder_traversal(tree_root)
    print("🟢", " → ".join(postorder))
else:
    print("🛑 No tree was created.")
