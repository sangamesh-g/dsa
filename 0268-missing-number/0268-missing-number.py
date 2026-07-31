class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i<n:
            j=nums[i]
            if n>j and nums[j]!=nums[i]:
                nums[j],nums[i]=nums[i],nums[j]

            else:
                i+=1
        for i in range(n):
            if i!=nums[i]:
                return i
        return n