# Using simple for loop

# a= [1,23,445,664,3,27,8,9,5]

# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# using the Tail recursion and print the array in reverse order
def Reverse(arr, i):
    if i == len(arr):
        return
    Reverse(arr,i+1)
    print(arr[i])

# here l and r is the index of arr
def recursion_reverse(arr,l,r):
    if l >=r:
        return
    arr[l],arr[r] = arr[r],arr[l]
    # below logic is not work
    # arr[l] = arr[r]
    # arr[r] = arr[l]
    # we need temp to swap
    # temp = arr[l]
    # arr[l] = arr[r]
    # arr[r] = temp
    recursion_reverse(arr,l+1,r-1)

def while_reverse(arr,l,r):
    while l<=r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr

if __name__ == '__main__':
    arr = [1,23,445,664,3,27,8,9,5]
    # Reverse(arr,0)
    # recursion_reverse(arr,0,len(arr)-1)
    arr = while_reverse(arr,0,len(arr)-1)
    print(arr)