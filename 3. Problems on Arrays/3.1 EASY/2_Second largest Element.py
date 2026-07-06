# BruteForce using sorting

def second_largest1(nums:list) ->int:

    nums.sort()

    return nums[-2]

# Better
def second_largest2(nums:list) -> int:

    n = len(nums)
    first_largest  = float("-inf")
    second_largest = float("-inf")

    for i in range(0,n):

        if nums[i] > first_largest:
            first_largest = nums[i]

    for i in range(0,n):

        #  if first_largest > nums [i] > second_largest :
        if nums[i]>second_largest and nums[i] != first_largest:
             second_largest = nums[i]

    return second_largest

# optimal solutions

def second_largest3(nums:list) ->int:

    n = len(nums)
    first_largest  = float("-inf")
    second_largest = float("-inf")

    for i in range(0,n):

        if nums[i] > first_largest:
            second_largest = first_largest
            first_largest = nums[i]
        elif nums[i] > second_largest and nums[i] != first_largest:
            second_largest = nums[i]

    return second_largest

if __name__ == '__main__':

    list1 = [1,4,75,58,9,99,77,102,-1,-6]
    list2 = [-1,-9,-89,-12,-52]
    list3 = [55,32,97,-55,45,32,88,21,97]
    print(second_largest1(list3))
    print(second_largest2(list3))
    print(second_largest3(list3))