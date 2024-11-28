arr = [1, 8, 4, 3, 3, 2, 7, 7, 7, 11, 9, 15, 23, 49]
left = 0
right = len(arr) - 1

print(right)

def quick_sort(arr, left, right):
    if left >= right:
        return
    
    p1, p2 = partition(arr, left, right)

    quick_sort(arr, left, p1 - 1)
    quick_sort(arr, p2 + 1, right)


def partition(arr, left, right):
    mid_value = (left + right) // 2
    pivot_value = sorted([arr[left], arr[mid_value], arr[right]])[1]

    if pivot_value == arr[mid_value]:
        arr[mid_value], arr[right] = arr[right], arr[mid_value]
    elif pivot_value == arr[left]:
        arr[left], arr[right] = arr[right], arr[left]    


    pivot = arr[right]
    i = left
    mid = left
    high = right - 1

    while mid <= high:
        if arr[mid] < pivot:
            arr[i], arr[mid] = arr[mid], arr[i]
            i += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    

    i += 1
    arr[mid], arr[right] = arr[right], arr[mid]
    return i, mid
    

quick_sort(arr, left, right)
print(arr)