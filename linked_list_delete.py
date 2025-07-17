class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def display():
    temp = head
    if not temp:
        print("List is empty.")
        return
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

def insert_at_end(data):
    global head
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node

def delete_from_beginning():
    global head
    if head is None:
        print("❌ List is empty.")
    else:
        print(f"✅ Deleted {head.data} from beginning.")
        head = head.next

def delete_from_end():
    global head
    if head is None:
        print("❌ List is empty.")
    elif head.next is None:
        print(f"✅ Deleted {head.data} from end.")
        head = None
    else:
        temp = head
        while temp.next.next:
            temp = temp.next
        print(f"✅ Deleted {temp.next.data} from end.")
        temp.next = None

def delete_at_position(position):
    global head
    if head is None:
        print("❌ List is empty.")
        return
    if position == 0:
        print(f"✅ Deleted {head.data} from position 0.")
        head = head.next
        return
    temp = head
    index = 0
    while temp.next and index < position - 1:
        temp = temp.next
        index += 1
    if temp.next is None:
        print("❌ Position out of range.")
    else:
        print(f"✅ Deleted {temp.next.data} from position {position}.")
        temp.next = temp.next.next

# User input loop for linked list operations
while True:
    print("\n----- Linked List Menu -----")
    print("1. Insert at end")
    print("2. Delete from beginning")
    print("3. Delete from end")
    print("4. Delete at position")
    print("5. Display list")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        val = int(input("Enter value to insert at end: "))
        insert_at_end(val)
        display()
    elif choice == '2':
        delete_from_beginning()
        display()
    elif choice == '3':
        delete_from_end()
        display()
    elif choice == '4':
        pos = int(input("Enter position to delete (0-based index): "))
        delete_at_position(pos)
        display()
    elif choice == '5':
        display()
    elif choice == '6':
        print("🚪 Exiting program.")
        break
    else:
        print("❗ Invalid choice. Please enter 1-6.")
