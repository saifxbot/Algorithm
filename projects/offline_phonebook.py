#selection sort implementation
def selection_sort(contacts): 
    n = len(contacts)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if contacts[j][0].lower() < contacts[min_idx][0].lower():
                min_idx = j
        contacts[i], contacts[min_idx] = contacts[min_idx], contacts[i]
    return contacts
# Phonebook application with linear search
def linear_search(contacts, target_name):
    for name, number in contacts:
        if name.lower() == target_name.lower():
            return number
    return None
#binary search
def binary_search(contacts, target_name):
    low = 0
    high = len(contacts) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_name = contacts[mid][0].lower()
        if mid_name == target_name.lower():
            return contacts[mid][1]
        elif mid_name < target_name.lower():
            low = mid + 1
        else:
            high = mid - 1
    return None

# Main Program
contacts = []

while True:
    print("\n Phonebook ")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search by name (Linear)")
    print("4. Search by name (Binary - sorted only)")
    print("5. Sort contacts by name")
    print("6. Exit")

    choice = input("Choose an option (1–6): ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        contacts.append((name, number))
        print("Contact added!")

    elif choice == "2":
        if not contacts:
            print("No contacts saved.")
        else:
            print("\nContacts:")
            for name, number in contacts:
                print(f"{name}: {number}")

    elif choice == "3":
        name = input("Enter name to search (linear): ")
        result = linear_search(contacts, name)
        print("Found!" if result else "Not found")
        if result:
            print(f"{name}: {result}")

    elif choice == "4":
        sorted_contacts = selection_sort(contacts.copy())
        name = input("Enter name to search (binary): ")
        result = binary_search(sorted_contacts, name)
        print("Found!" if result else "Not found")
        if result:
            print(f"{name}: {result}")

    elif choice == "5":
        contacts = selection_sort(contacts)
        print("Contacts sorted by name.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
