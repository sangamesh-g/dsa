class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=set(nums)
        for ans in range(1,len(nums)+2):
            if ans not in nums:
                return ans
