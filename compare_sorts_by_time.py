import time
import copy
import heapq

# -------- Sorting Algorithms -------- #

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

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)

def heap_sort(arr):
    heapq.heapify(arr)
    arr[:] = [heapq.heappop(arr) for _ in range(len(arr))]

# -------- Timing Helper -------- #

def time_sort(name, func, data, results):
    arr = copy.deepcopy(data)
    start = time.time()
    func(arr)
    end = time.time()
    duration = round((end - start) * 1000, 4)
    results.append((name, duration))
    print(f"{name}:")
    print("Sorted:", arr)
    print("Time:  ", duration, "ms\n")

# -------- Main -------- #

user_input = input("Enter numbers separated by space: ")
original = [int(x) for x in user_input.strip().split()]

results = []

print("\n🔵 Sorting Results:\n")

time_sort("Bubble Sort", bubble_sort, original, results)
time_sort("Selection Sort", selection_sort, original, results)
time_sort("Insertion Sort", insertion_sort, original, results)
time_sort("Merge Sort", merge_sort, original, results)
time_sort("Quick Sort", quick_sort, original, results)
time_sort("Heap Sort", heap_sort, original, results)

# -------- Best/Worst Summary -------- #
results.sort(key=lambda x: x[1])
print("📊 Summary:")
print(f" Fastest: {results[0][0]} ({results[0][1]} ms)")
print(f" Slowest: {results[-1][0]} ({results[-1][1]} ms)")
