import time

# Array insertion at beginning
arr = [i for i in range(100000)]  # Create an array with 100000 elements

start_time = time.time()
arr.insert(0, -1)  #(0, -1) means inserting at the beginning
end_time = time.time()

print(f"Array insertion took {end_time - start_time:.6f} seconds")

# Linked List Setup
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

def insert_at_beginning(data):
    global head
    new_node = Node(data)
    new_node.next = head
    head = new_node

# Create linked list with 100000 nodes
for i in range(100000):
    insert_at_beginning(i)

# Now measure insertion time at beginning
start_time = time.time()
insert_at_beginning(-1) #(-1) means inserting at the beginning
end_time = time.time()

print(f"Linked list insertion took {end_time - start_time:.6f} seconds")
