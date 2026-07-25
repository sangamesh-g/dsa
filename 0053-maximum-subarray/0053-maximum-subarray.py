class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=-float('inf')
        curr=0
        for i in nums:
            if curr<0:
                curr=i
            else:
                curr+=i
            if curr>ans:
                ans=curr
        return ans