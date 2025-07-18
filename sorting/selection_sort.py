def selection_sort(arr):
    n = len(arr)
    for i in range(n):                                 # iterate through each index in the array
        min_index = i                                  # present index is assumed to be the minimum
        for j in range(i + 1, n):                      # iterate through the unsorted part of the array
            if arr[j] < arr[min_index]:                # if a smaller element is found
                min_index = j                          # found a new minimum
                                                       # swap the found minimum with the current index
        arr[i], arr[min_index] = arr[min_index], arr[i]# swap the elements to place the minimum at the current index

                                                       
                                                       
data = [64, 25, 12, 22, 11]                            # Example array to sort
print("Before sorting:", data)

selection_sort(data)

print("After sorting:", data)
