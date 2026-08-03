class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        ans=[]
        while i<n:
            j=nums[i]-1
            if j<n and nums[i]-1!=nums[j]-1:
                nums[j],nums[i]=nums[i],nums[j]
            else:
                i+=1
        for i in range(n):
            if i+1!=nums[i]:
                ans.append(i+1)
        return ans