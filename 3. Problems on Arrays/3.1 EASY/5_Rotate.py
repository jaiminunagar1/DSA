nums = [7,10,5,-2,2,3,4,6]
n = len(nums)
print(f"before rotating : {nums}")
nums[:] = [nums[-1]] + nums[0:len(nums)-1]
nums[:] = [nums[n-1]]+nums[:len(nums)-1]
print(f"after rotation2: {nums}")


# without slicing
# temp = nums[n-1]
# for i in range(n-2,-1,-1):
#     nums[i+1]=nums[i]
# nums[0] = temp
