def twosum1(nums:list,target:int)->list:
    result = []
    n = len(nums)

    for i in range(0,n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return [i,j]

def twosum2(nums:list,target:int) ->list:
        hash_map = {}
        n = len(nums)
        for i in range(0,n):
            # print(f"hash_map = {hash_map}")
            remaining = target-nums[i]
            if remaining in hash_map:
                print(remaining)
                return [hash_map[remaining],i]
            hash_map[nums[i]]=i

if __name__ == "__main__":
    nums = [5,9,1,2,4,15,6,3]
    print(twosum1(nums,13))
    print(twosum2(nums,13))