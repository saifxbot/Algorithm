class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

head = None

def insert_at_beginning(data):
    global head
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    head = new_node
    print(f"✅ Inserted {data} at beginning.")

def insert_at_end(data):
    global head
    new_node = Node(data)
    if head is None:
        head = new_node
        print(f"✅ Inserted {data} as the first node.")
        return
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp
    print(f"✅ Inserted {data} at end.")

def delete_from_beginning():
    global head
    if head is None:
        print("❌ List is empty, nothing to delete.")
        return
    print(f"✅ Deleted {head.data} from beginning.")
    head = head.next
    if head:
        head.prev = None

def delete_from_end():
    global head
    if head is None:
        print("❌ List is empty, nothing to delete.")
        return
    if head.next is None:
        print(f"✅ Deleted {head.data}, list is now empty.")
        head = None
        return
    temp = head
    while temp.next:
        temp = temp.next
    print(f"✅ Deleted {temp.data} from end.")
    temp.prev.next = None

def display_forward():
    temp = head
    if temp is None:
        print("List is empty.")
        return
    print("Forward traversal: ", end="")
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

def display_backward():
    temp = head
    if temp is None:
        print("List is empty.")
        return
    while temp.next:
        temp = temp.next
    print("Backward traversal: ", end="")
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.prev
    print("None")

# Main menu loop
while True:
    print("\n--- Doubly Linked List Menu ---")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Delete from beginning")
    print("4. Delete from end")
    print("5. Display forward (Traversal)")
    print("6. Display backward (Traversal)")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        val = int(input("Enter value to insert at beginning: "))
        insert_at_beginning(val)
    elif choice == '2':
        val = int(input("Enter value to insert at end: "))
        insert_at_end(val)
    elif choice == '3':
        delete_from_beginning()
    elif choice == '4':
        delete_from_end()
    elif choice == '5':
        display_forward()
    elif choice == '6':
        display_backward()
    elif choice == '7':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter 1-7.")
