# binary search algorithm

def binarySearch(item, arr):
    arraySize = len(arr) - 1
    lowerIdx = 0
    upperIdx =arraySize

    while lowerIdx <= upperIdx:
        # find a middle point of the array
        middlePoint = (lowerIdx + upperIdx) // 2

        # if we found the item then return the index
        if arr[middlePoint] == item:
            return middlePoint

        # looking for a new middle point in the right or in the left half of the array
        if item > arr[middlePoint]:
            lowerIdx = middlePoint + 1
        else:
            upperIdx = middlePoint - 1

    if lowerIdx > upperIdx:
        return None


# test
items = [-3,4,5,7,9,14,26,37,345]
print(binarySearch(1, items))
print(binarySearch(26, items))
print(binarySearch(-3, items))