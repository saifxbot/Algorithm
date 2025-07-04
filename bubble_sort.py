#Bubble sort algorithm implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False                                 # Swap flag to check if any swapping happened
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                                                        # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break                                       # If no two elements were swapped, the array is sorted

# Example usage       ---    takes a lot of time
if __name__ == "__main__":
    numbers = [64, 25, 12, 22, 11]
    print("Before sorting:", numbers)
    bubble_sort(numbers)
    print("After sorting:", numbers)
# time complexity: O(n^2) in worst case, O(n) in best case (when the array is already sorted)
# space complexity: O(1) as it sorts in place