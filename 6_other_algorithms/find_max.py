# find max element using recursion


# create a Hashtable
def findMax(arr):
    # breacking condition: if it's the last item in the arraythen return it
    if len(arr) == 1:
        return arr[0]

    # otherwise get the first item and call function again
    # to operate it on the rest of the array
    el1 = arr[0]
    el2 = findMax(arr[1:])

    # when we came to just two elements
    if el1 > el2:
        return el1
    else:
        return el2


# test
items = [2,6,34,678,123124,123124]
print(findMax(items))