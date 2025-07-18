def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid          # target found, return index
        elif arr[mid] < target:
            low = mid + 1       # move to the right half
        else:
            high = mid - 1      

    return -1                   # target not found, return -1

arr = [1, 3, 5, 7, 9, 11]       # Example sorted array
print(binary_search(arr, 7))    # Output: 3 (index)
print(binary_search(arr, 4))    # Output: -1 (not found)
                                # Best case: O(1) (target is the middle element)
                                # Worst case: O(log n) (target is not present or at the ends) 
                                # Average case: O(log n) (target is somewhere in the array)
                                # Space complexity: O(1) (no additional space used)
