# Selection Sort
def selection_sort(students):
    n = len(students)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if students[j][1] < students[min_idx][1]:
                min_idx = j
        students[i], students[min_idx] = students[min_idx], students[i] # Swap the found minimum with the current index
                                                     # Return the sorted list of students
    return students

# Linear Search
def linear_search(students, target):
    for name, mark in students:              # Iterate through each student
        if mark == target:                   # If the mark matches the target
            return name
    return None

# Binary Search
def binary_search(students, target):
    low = 0
    high = len(students) - 1             # Ensure the list is sorted before binary search
    while low <= high:
        mid = (low + high) // 2
        if students[mid][1] == target:   # If the mark at mid index matches the target
            return students[mid][0]      # Return the name of the student with the target mark
        elif students[mid][1] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# --- Main Program starts ---
students = []

# Input student data
n = int(input("How many students you like to add in the array? "))
for _ in range(n):                     # Loop to input student names and marks
    name = input("Enter student name: ")
    mark = int(input("Enter student mark: "))
    students.append((name, mark))

print("\nOriginal student list:")
print(students)

# addded loop for the users to choose the desired operation until they exit
while True:
    print("\nWhat would you like to do?")
    print("1. Sort by marks")
    print("2. Search a mark (linear search)")
    print("3. Search a mark (binary search — sorted list)")
    print("4. Exit")

    choice = int(input("Enter your choice (1–4): "))

    if choice == 1:
        sorted_students = selection_sort(students.copy())
        print("\nSorted list by marks:")
        print(sorted_students)

    elif choice == 2:
        target = int(input("Enter the mark to search (linear): "))
        result = linear_search(students, target)
        print("Found:", result if result else "Not found")

    elif choice == 3:
        sorted_students = selection_sort(students.copy())
        target = int(input("Enter the mark to search (binary): "))
        result = binary_search(sorted_students, target)
        print("Found:", result if result else "Not found")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please choose 1 to 4.")
