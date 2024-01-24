def binary_search(arr1, down, high, x):
    if high >= down:
        mid = (high + down) // 2
        if arr1[mid] == x:
            return mid
        elif arr1[mid] > x:
            return binary_search(arr1, down, mid - 1, x)
        else:
            return binary_search(arr1, mid + 1, high, x)
    else:
        return -1

arr1 = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr1, 0, len(arr1)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
