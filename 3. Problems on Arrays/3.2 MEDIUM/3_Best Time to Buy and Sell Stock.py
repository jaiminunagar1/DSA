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


def maxiprofit2(prices:list[int])->int:
    max_profit = 0
    mini_price = float("inf")
    n = len(prices)
    for i in range(0,n):
        if prices[i]<mini_price:
            mini_price = prices[i]
        if prices[i]>mini_price:
            profit = prices[i]-mini_price
            if profit>max_profit:
                max_profit = profit
    return max_profit


if __name__ == "__main__":
    nums = [7,2,1,5,6,4,8]
    nums2 = [1,2]
    # print(maxiprofit(nums2))
    print(maxiprofit2(nums2))