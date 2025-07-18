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
    print(f"✅ {data} inserted at beginning.")

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
    print(f"✅ {data} inserted at end.")

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
    print(f"✅ {data} inserted at position {position}.")

# Main Program Loop
while True:
    print("\n----- Linked List Menu -----")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at specific position")
    print("4. Display list")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

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
        display()
    elif choice == '5':
        print("🚪 Exiting program.")
        break
    else:
        print("❗ Invalid choice. Please enter 1-5.")
