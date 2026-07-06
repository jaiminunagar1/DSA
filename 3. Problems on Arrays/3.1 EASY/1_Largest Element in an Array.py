# Method 1

def largest1(nums:list) ->int:
    n = len(nums)
    largest = nums[0]
    for i in range(0,n):
        if nums[i] > largest:
            largest= nums[i]
    return largest

def largest2(nums:list) ->int:
    n = len(nums)
    largest = nums[0]
    for i in range(0,n):
        largest = max(largest,nums[i])
    return largest


# Method 2


def largest3(nums:list) ->int:
    n = len(nums)
    largest = float("-inf")

    for i in range(0,n):
        if nums[i] > largest:
            largest = nums[i]
    return largest

if __name__ == '__main__':

    list1 = [1,4,75,58,9,99,77,102,-1,-6]
    list2 = [-1,-9,-89,-12,-52]
    print(largest1(list2))
    print(largest2(list2))
    print(largest3(list2))