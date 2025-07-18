def linear_search(arr, target):
    for index, item in enumerate(arr): # enumerate provides both index and item
        if item == target:
            return index               # target found, return index
    return -1                          # target not found

data = [4, 2, 7, 1, 9]
print(linear_search(data, 7))          # Output: 2 (index of 7)
print(linear_search(data, 5))          # Output: -1 (not found)
                                       # best case: O(1) (target is the first element)
                                       # worst case: O(n) (target is the last element or not present)
                                       # average case: O(n) (target is somewhere in the middle)
                                       # space complexity: O(1) (no additional space used)