import time             # Importing time module to measure execution time
import copy             # Importing copy module to create deep copies of lists


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Helper to measure time in ms
def time_sort(sort_func, data):        # data is the list to be sorted
    arr = copy.deepcopy(data)          # Create a copy to avoid modifying the original list
    start = time.time()                
    sort_func(arr)                     
    end = time.time()
    elapsed_ms = (end - start) * 1000  # converted to milliseconds
    return arr, round(elapsed_ms, 4)   # rounding to 4 decimal places


# Main test
original_list = [9, 5, 2, 7, 3, 8, 6, 1, 4, 0]

# Bubble Sort
sorted_bubble, time_bubble = time_sort(bubble_sort, original_list)
print("🔵 Bubble Sort:")
print("Sorted:", sorted_bubble)
print("Time:  ", time_bubble, "ms\n")

# Selection Sort
sorted_selection, time_selection = time_sort(selection_sort, original_list)
print("🟡 Selection Sort:")
print("Sorted:", sorted_selection)
print("Time:  ", time_selection, "ms\n")

# Insertion Sort
sorted_insertion, time_insertion = time_sort(insertion_sort, original_list)
print("🟢 Insertion Sort:")
print("Sorted:", sorted_insertion)
print("Time:  ", time_insertion, "ms")
