class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}
        for i in range(n):
            k=target- nums[i]
            if k in d:
                return [d[k],i]
            d[nums[i]]=i