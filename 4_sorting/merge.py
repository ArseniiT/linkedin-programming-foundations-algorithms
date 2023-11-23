# merge sort algorithm

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftArr = arr[:mid]
        rigthArr = arr[mid:]

        # breack down the array recursively
        mergeSort(leftArr)
        mergeSort(rigthArr)

        # here we are perfoming the merging
        i = 0 # index of the left arr
        j = 0 # index of the right arr
        k = 0 # index of the merged arr

        # while right and left parts of original array have content
        while i < len(leftArr) and j < len(rigthArr):
            if leftArr[i] < rigthArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rigthArr[j]
                j += 1
            k += 1

        # if the left part of the array still has values, add them
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        # if the rigth part of the array still has values, add them
        while j < len(rigthArr):
            arr[k] = rigthArr[j]
            j += 1
            k += 1


# test
items = [3,4,5,67,1,2,4,5,-78,2,23325,-34454]
print(items)
mergeSort(items)
print(items)
