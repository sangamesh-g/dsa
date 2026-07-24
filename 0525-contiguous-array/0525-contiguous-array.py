class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans=0
        prefdict={0:-1}
        prefix=0
        for i in range(len(nums)):
            if nums[i]==0:
                prefix-=1
            else:
                prefix+=1
            if prefix in prefdict:
                ans=max(ans,i-prefdict[prefix])
            else:
                prefdict[prefix]=i
        return ans