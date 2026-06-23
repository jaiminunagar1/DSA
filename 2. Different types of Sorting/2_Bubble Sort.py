def bubbleSort_ASC(arr:list)->list:
    size=len(arr)
    for _ in range(0,size):
        is_swap = False
        for i in range(0,size-1):
            # print(i)
            j=i+1
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                is_swap = True
        if is_swap == False:
            break
        size-=1
    return arr


def bubbleSort_DESC(arr:list)->list:
    size=len(arr)
    for _ in range(0,size):
        is_swap = False
        for i in range(0,size-1):
            # print(i)
            j=i+1
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                is_swap = True
        if is_swap == False:
            break
        size-=1
    return arr

# In Video

def bubbleSort_ASC1(arr:list)->list:
    size = len(arr)
    for i in range(size-2,-1,-1):
        is_swap = False
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                is_swap = True
        if is_swap == False:
            break
    return arr

if __name__ == '__main__':
    arr = [5,8,1,6,9,2,4]
    Ans1 = bubbleSort_ASC(arr.copy())
    Ans2 = bubbleSort_DESC(arr.copy())
    Ans3 = bubbleSort_ASC1(arr.copy())
    print(Ans1)
    print(Ans2)
    print(Ans3)

