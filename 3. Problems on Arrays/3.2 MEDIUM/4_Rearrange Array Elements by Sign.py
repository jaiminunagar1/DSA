def rearrange(nums:list[int])->list[int]:
    n = len(nums)
    pos = []
    neg = []
    for i in range(0,n):
        if nums[i]>0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    for i in range(0,len(neg)):
        nums[2*i] = pos[i]
        nums[(2*i)+1] = neg[i]
    return nums

def rearrange2(nums:list[int])->list[int]:
    n = len(nums)
    posIndx,negIndx = 0,1
    result = [0]*n
    for i in range(0,n):
        if nums[i] > 0:
            result[posIndx]=nums[i]
            posIndx+=2
        else:
            result[negIndx] = nums[i]
            negIndx+=2
    return result


if __name__ == "__main__":
    nums = [3,1,-2,-5,2,-4]
    print(rearrange(nums.copy()))
    print(rearrange2(nums.copy()))

