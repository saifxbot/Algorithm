def quick_sort(arr):
    if len(arr) <= 1:                                 # Base case for recursion
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]         # Elements less than or equal to pivot
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

# User input
user_input = input("Enter numbers separated by space: ")
numbers = list(map(int, user_input.strip().split()))  # Convert input to list of integers

sorted_numbers = quick_sort(numbers)
print("Sorted (Quick Sort):", sorted_numbers)
