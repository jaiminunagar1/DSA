def partition(arr,low,high):

    i,j = low,high
    pivot = arr[low]

    while i<j:

        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]> pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[j],arr[low] = arr[low],arr[j]

    return j


def quick_sort(nums,low,high):
    if low<high:
      pindex =  partition(nums,low,high)
      quick_sort(nums,low,pindex-1)
      quick_sort(nums,pindex+1,high)

if __name__ == '__main__':

    arr = [4,7,8,3,2,1]
    # print(partition(arr,0,len(arr)-1))
    quick_sort(arr,low=0,high=len(arr)-1)
    print(arr)

        