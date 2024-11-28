arr = [3, 2, 42, 21, 12, 1, 10, 50, 49]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


print(f"Sorted array: {bubble_sort(arr)}")