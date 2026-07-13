def RightRotate1(nums:list,k:int):
    n  = len(nums)
    i = 1
    while i<=k:
        temp = nums[n-1]
        for j in range(n-2,-1,-1):
            nums[j+1] = nums[j]
        nums[0]=temp
        i+=1
    return nums


def RightRotate2(nums:list,k:int):
    n  = len(nums)
    for _ in range(0,k):
        temp = nums[n-1]
        for j in range(n-2,-1,-1):
            nums[j+1] = nums[j]
        nums[0]=temp
    return nums

def RightRotate3(nums:list,k:int):
    
    for _ in range(0,k):
        e = nums.pop()
        nums.insert(0,e)

# Optimal


def RightRotate4(nums:list,k:int):

    n=len(nums)
    k = k % n   
    nums[:] = nums[n-k:]+nums[:n-k]

def reverse(nums:left,right):

    while left <= right :
        arr[left],arr[right] = arr[right],arr[left]
        left +=1
        right+=1

if __name__=="__main__":

    arr = [3,9,5,6,7,2]
    print(RightRotate1(arr,3))
    n = len(arr)
    # k = k % n
    k = 4
    reverse(arr,n-k,n-1)
    reverse(arr,0,n-k-1)
    reverse(arr,0,n-1)

    
