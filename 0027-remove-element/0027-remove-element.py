class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        i=0
        n=len(nums)
        while i<n:
            if nums[i]!=val:
                nums[j]=nums[i]
                j+=1
            i+=1
        return j