def selectionSort_ASC(arr):
        min_index = 0
        for i in range(0,len(arr)):
            min_index = i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_index]:
                    min_index = j
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr

def selectionSort_Desc(arr):
        for i in range(0,len(arr)):
            max_index = i
            for j in range(i+1,len(arr)):
                if arr[j]>arr[max_index]:
                      max_index = j
            arr[i],arr[max_index]=arr[max_index],arr[i]
        return arr

if __name__ == '__main__':
    arr = [7,9,5,3,1,2,4]
    sort_arr = selectionSort_ASC(arr.copy())
    desc_sort = selectionSort_Desc(arr.copy())
    print(sort_arr)
    print(desc_sort)