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

def insert_at_beginning(data):
    global head
    new_node = Node(data)
    new_node.next = head
    head = new_node
    print(f"✅ Inserted {data} at beginning.")

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
    print(f"✅ Inserted {data} at end.")

def insert_at_position(data, position):
    global head
    new_node = Node(data)
    if position == 0:
        insert_at_beginning(data)
        return
    temp = head
    index = 0
    while temp and index < position - 1:
        temp = temp.next
        index += 1
    if temp is None:
        print("❌ Position out of range.")
        return
    new_node.next = temp.next
    temp.next = new_node
    print(f"✅ Inserted {data} at position {position}.")

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

# Main Menu
while True:
    print("\n----- Linked List Menu -----")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at position")
    print("4. Delete from beginning")
    print("5. Delete from end")
    print("6. Delete at position")
    print("7. Display list")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        val = int(input("Enter value to insert at beginning: "))
        insert_at_beginning(val)
        display()
    elif choice == '2':
        val = int(input("Enter value to insert at end: "))
        insert_at_end(val)
        display()
    elif choice == '3':
        val = int(input("Enter value to insert: "))
        pos = int(input("Enter position (0-based index): "))
        insert_at_position(val, pos)
        display()
    elif choice == '4':
        delete_from_beginning()
        display()
    elif choice == '5':
        delete_from_end()
        display()
    elif choice == '6':
        pos = int(input("Enter position to delete (0-based index): "))
        delete_at_position(pos)
        display()
    elif choice == '7':
        display()
    elif choice == '8':
        print("🚪 Exiting program.")
        break
    else:
        print("❗ Invalid choice. Please enter 1-8.")
