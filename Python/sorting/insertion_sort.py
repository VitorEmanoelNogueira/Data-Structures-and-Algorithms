array = [23, 21, 29, 95, 2, 21, 1, 42, 50, 15]

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        current_value = array[i]
        j = i -1
        while j >= 0 and array[j] > current_value:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current_value
    return array

print(f"Sorted array: {insertion_sort(array)}")