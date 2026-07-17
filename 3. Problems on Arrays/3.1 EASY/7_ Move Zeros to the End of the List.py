def MoveZeroEnd(nums:list):
    n = len(nums)
    temp = []

    for i in range(0,n):
        if nums[i] != 0:
            temp.append(nums[i])
    for i in range(0,n):
        if i < len(temp):
            nums[i] = temp[i]
        else:
            nums[i] = 0    
    