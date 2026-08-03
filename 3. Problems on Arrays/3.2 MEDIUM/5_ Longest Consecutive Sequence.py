# BruteForce
def maxsequ1(nums:list[int]) ->int :
    max_seq = 0    
    n = len(nums)
    for i in range(0,n):
        seq = nums[i]
        count = 1
        while seq+1 in nums:
                count +=1
                seq = seq + 1
        if count > max_seq:
            max_seq = count
    return max_seq


# optimial not give the timelimit exceed error

def mqxsequ2(nums:list[int]) ->int:
    n = len(nums)
    nums.sort()
    count = 0
    last_smaller = float("-inf")
    longest = 0
    for i in range(0,n):
        num = nums[i]
        if last_smaller == num-1:
            last_smaller = num
            count +=1
        elif num != last_smaller:
            last_smaller = num
            count = 1
        if count > longest:
            longest = count
    return longest

# best (Give the time limiy exceed error in leet code)

def mqxsequ3(self, nums: list[int]) -> int:
        n= len(nums) 
        my_set = set()
        for i in range(0,n):
            my_set.add(nums[i])
        longest_seq = 0
        for i in range(0,n):
            num = nums[i]
            if num-1 not in my_set:
                count=1
                x = num
                while x+1 in my_set:
                    count+=1
                    x+=1
                if count>longest_seq:
                    longest_seq = count
        return longest_seq

if __name__ =="__main__":
    nums = [100,4,200,1,3,2]
    print(maxsequ1(nums))
    print(mqxsequ2(nums))