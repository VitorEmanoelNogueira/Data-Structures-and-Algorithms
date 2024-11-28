import math

def merge_sort(arr): # O(log n)
    if len(arr) < 2:
        return arr
    
    middle_index = math.floor(len(arr) / 2)
    left_arr = arr[:middle_index]
    right_arr = arr[middle_index:]

    return merge(merge_sort(left_arr), merge_sort(right_arr)) #O(n)

# O(n log n)


def merge(left_arr, right_arr):
    result_arr = []
    left_index = 0
    right_index = 0

    while(left_index < len(left_arr) and right_index < len(right_arr)):
        if(left_arr[left_index] < right_arr[right_index]):
            result_arr.append(left_arr[left_index])
            left_index += 1
        else:
            result_arr.append(right_arr[right_index])
            right_index += 1
    
    result_arr.extend(left_arr[left_index:])
    result_arr.extend(right_arr[right_index:])
    return result_arr


arr = [12, 3, 16, 6, 5, 1]
print(merge_sort(arr))