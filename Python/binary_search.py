import math

arr = []
start = 0
target =  500

for i in range(1025):
    arr.append(i)

end = len(arr) - 1



def binary_search(arr, start, end, target):
    print(arr[start:end])
    if start > end:
        return False

    mid_index = math.floor((start + end) / 2)
    if arr[mid_index] == target:
        return True
    elif arr[mid_index] > target:
        return binary_search(arr, start, mid_index-1, target)
    else:
        return binary_search(arr, mid_index+1, end, target)

    
print(binary_search(arr, start, end, target))