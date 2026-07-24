class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans=0
        prefdict={0:-1}
        prefix=0
        for i,num in enumerate(nums):
            prefix += -1 if num == 0 else 1
            if prefix in prefdict:
                ans=max(ans,i-prefdict[prefix])
            else:
                prefdict[prefix]=i
        return ans