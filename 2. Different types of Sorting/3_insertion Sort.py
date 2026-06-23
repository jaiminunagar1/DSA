def insertionSort(arr:list) ->list:
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            k = arr[i]
            for j in range(i-1,-1,-1):
                if arr[j]>k:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


def insertionSort_ASC(arr:list) ->list:
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    return arr

def insertionSort_DESC(arr:list) ->list:
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]<key:
            arr[j+1] = arr[j] 
            j = j-1
        arr[j+1] = key
    return arr


if __name__ == '__main__':
    arr = [5,8,1,6,9,2,4]
    Ans1 = insertionSort(arr.copy())
    Ans2 = insertionSort_ASC(arr.copy())
    Ans3 = insertionSort_DESC(arr.copy())
    print(Ans1)
    print(Ans2)
    print(Ans3)

