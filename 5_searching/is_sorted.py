# determine if an array is sorted

def isSorted(arr):
    # using the brute force method
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False

    return True

def isSortedPyVersion(arr):
    # using Python function method
    return all(arr[i] < arr[i+1] for i in range(len(arr) - 1))


# test
items1 = [1,2,3,4,5,6,7,8,9]
items2 = [4,-3,5,1,6,2,7,89,3]

print(isSorted(items1))
print(isSorted(items2))

print(isSortedPyVersion(items1))
print(isSortedPyVersion(items2))