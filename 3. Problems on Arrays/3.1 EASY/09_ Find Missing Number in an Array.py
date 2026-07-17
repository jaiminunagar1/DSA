def findmissing1(nums: list) -> int:
    n = len(nums)
    for i in range(0, n + 1):
        found = False
        for j in range(0, n):
            if nums[j] == i:
                found = True
                break  # We found 'i', so we can stop searching the rest of the list
        
        # If we finished looking through the list and never found 'i', it's the missing one!
        if not found:
            return i

def findmissing2(nums:list):
    n = len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i
# Optimial
        # better
def findmissing3(nums:list):
    n = len(nums)
    dict = {}
    for i in range(0,n+1):
        dict[i]=0
    for i in range(0,n):
        dict[nums[i]]=1
    print(dict)
    for i in range(0,n+1):
        print(f"{i} is and dict[i] is {dict[i]}")
        if dict[i]==0:
            return i
    

# best optimial
def findmissing4(nums:list):
    sum = 0
    result = 0
    n = len(nums)
    for i in range(0,n+1):
        sum +=i
    for i in range(0,n):
        result+=nums[i]
    ans = sum - result
    return ans


if __name__ == "__main__":
    nums = [1, 0]
    print(findmissing3(nums=nums))  # Outputs: 2