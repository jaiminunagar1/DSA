def maxcount(nums:list):
    max = 0
    count = 0
    n = len(nums)
    for i in range(0,n):
        if nums[i] == 1:
            j=i
            while j < n and nums[j]==1:
                if nums[j]==1:
                    count+=1
                    j+=1
                else:
                    break
        if max<count:
            max = count
        count = 0
    return max


def maxcount2(nums:list):
    max_seq = 0
    count = 0
    n = len(nums)
    for i in range(0,n):
        if nums[i] == 1:
            count+=1
        else:
            if max_seq<count:
                max_seq= count
            count = 0
    max_seq = max(max_seq,count)
    return max_seq

if __name__ == "__main__":
    nums = [1,1,0,1,0,1,1,1,1,0,1,1]
    print(maxcount(nums=nums))
    print(maxcount2(nums=nums))
