def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == "__main__":
    arr = [3, 6, 2, 8, 9, 10, 12, 25, 39, 48]
    target = 25
    result = linear_search(arr, target)

    if result != -1:
        print(f"Value {target} found at index {result}.")
    else:
        print(f"Value {target} was not found.")

