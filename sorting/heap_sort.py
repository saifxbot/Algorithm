def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Step 1: Max-Heap build
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap max to end
        heapify(arr, i, 0)

# User input
nums = list(map(int, input("Enter numbers (space-separated): ").split()))
heap_sort(nums)
print("Sorted list:", nums)
