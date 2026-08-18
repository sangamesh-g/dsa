class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev=-float('inf')
        ans=nums[0]
        for i in range(len(nums)):
            if nums[i]<prev:
                ans=nums[i]
            prev=nums[i]
        return ans