def maxisum(nums:list)->list:
    n = len(nums)
    maxi = float("-inf")
    # total = 0
    for i in range(0,n):
        total = 0
        for j in range(i,n):
            total = total+nums[j]
            if total > maxi:
                maxi = total
    return maxi


# optomal solution 

# Kaden solution

def maxisum2(nums:list):
    maxi = float("-inf")
    total = 0
    n = len(nums)
    for i in range(0,n):
        total = total+nums[i]
        if maxi<total:
            maxi = total
        if total<0:
            total = 0
    return maxi

if __name__ == "__main__":
    nums = [-2,1,3,4,-1,2,1,-5,4]
    print(maxisum(nums))
    print(maxisum2(nums))    