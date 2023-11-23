# bubble sort algorithm

def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
        print(arr)


def main():
    list1 = [5,2,2,4,6,1,7,123,3,0,-2]
    bubbleSort(list1)
    print("Sort result: ", list1)

if __name__ == "__main__":
    main()