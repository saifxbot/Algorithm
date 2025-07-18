class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

# Recursive display function
def recursive_display(node):
    if node is None: 
        print("None")
        return
    print(node.data, end=" -> ")
    recursive_display(node.next)
#recursive traversal is used to display the linked list


# Linked list: 10 -> 20 -> 30 -> None
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

recursive_display(head)
