def linear_search(arr, target):
    # Your code here
    for index in range(len(arr)):
        if arr[index] == target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Searcht
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            low = mid+1
        elif (arr[mid] > target):
            high = mid-1

    return -1  # not found
