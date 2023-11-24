# quick sort algorithm

def quickSort(arr, first, last):
    if first <  last:
        # calculate the split point
        pivotIndex = partition(arr, first, last)

        # sort the two partition
        quickSort(arr, first, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, last)


def partition(arr, first, last):
    # choose the fisrt value as the pivot value
    pivotValue = arr[first]

    # establish the upper and the lower indexes
    lower = first + 1
    upper = last

    # start serching for the crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and arr[lower] <= pivotValue:
            lower += 1

        # advance the upper index
        while lower <= upper and arr[upper] >= pivotValue:
            upper -= 1

        # when the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            tmp = arr[lower]
            arr[lower] = arr[upper]
            arr[upper] = tmp

    # when the split point is found, exchange the pivot value
    tmp = arr[first]
    arr[first] = arr[upper]
    arr[upper] = tmp

    # return the split point index
    return upper


# test

items = [5,3,1,-5,566,-456457,64,6,7,2,0]

print(items)
quickSort(items, 0, len(items) - 1)
print(items)
