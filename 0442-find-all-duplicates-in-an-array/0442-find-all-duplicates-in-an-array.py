class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        n=len(nums)
        while i<n:
            j=nums[i]-1
            if 1<=nums[i]<=n and nums[i]!=nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
            else:
                i+=1
        print(nums)
        for i in range(n):
            if nums[i]!=i+1:
                ans.append(nums[i])
            
        return ans