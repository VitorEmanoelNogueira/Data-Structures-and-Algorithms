arr = [23, 411, 22, 39, 5, 39, 12, 1, 5, 7, 90]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

print(f"Sorted array: {selection_sort(arr)}")