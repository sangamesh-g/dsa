class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        while i<n:
            j=nums[i]-1
            if 1 <= nums[i] <= n and nums[i]!=nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1
        print(nums)
        for i in range(n):
            if i+1!=nums[i] and i+1>0:
                return i+1
        return n+1