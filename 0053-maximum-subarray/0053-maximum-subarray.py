class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        ans=curr
        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            ans=max(curr,ans)
        return ans