def maxiprofit(nums:list) -> int:
    max_profit = 0
    profit = 0
    n = len(nums)
    for i in range(0,n):
        # print(i)
        for j in range(i+1,n):
            # print(f" when i {i} then j is {j}")
            if nums[j]>nums[i]:
                profit = nums[j]-nums[i]
                if profit>max_profit:
                    max_profit = profit
    return max_profit

if __name__ == "__main__":
    nums = [7,2,1,5,6,4,8]
    print(maxiprofit(nums))