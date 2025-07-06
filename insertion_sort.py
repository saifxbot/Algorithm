def insertion_sort(arr):
    for i in range(1, len(arr)):       # Start from the second element
        key = arr[i]                   # Element to be inserted
        j = i - 1                      # Index of the previous element

        while j >= 0 and arr[j] > key: # Shift elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            arr[j + 1] = arr[j]        
            j -= 1                     # Move to the previous element

        arr[j + 1] = key

# Example usage
numbers = [8, 4, 2, 9, 1, 5]
print("Before sorting:", numbers)


insertion_sort(numbers)

# After sorting
print("After sorting:", numbers)
