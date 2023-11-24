# unordered search or Linear search

def findIndexOfItem(item, arr):
    for i in range(0, len(arr)):
        if item == arr[i]:
            return i
    return None


# test
items = [5,7,3,6,444,-78,435,0]
print(findIndexOfItem(6, items))
print(findIndexOfItem(445, items))