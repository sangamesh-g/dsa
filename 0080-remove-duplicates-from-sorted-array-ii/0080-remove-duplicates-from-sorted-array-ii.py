class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=2
        i=len(nums)-1
        while(j<len(nums)):
            if nums[j]==nums[j-2]:
                del nums[j]
            else:
                j+=1