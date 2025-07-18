def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Merge two sorted halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Add remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# 🔸 Take user input
user_input = input("Enter numbers separated by space: ")

# Convert input to list of integers
arr = list(map(int, user_input.strip().split()))

# Sort using merge sort
sorted_arr = merge_sort(arr)

# Show result
print("✅ Sorted array:", sorted_arr)  # time complexity: O(n log n), space complexity: O(n)
