class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans=1
        nums=set(nums)
        while ans<=len(nums)+1:
            if ans not in nums:
                return ans
            ans+=1