class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=2
        for n in nums[2:]:
            if n!=nums[i-2]:
                nums[i]=n
                i+=1
        return i
