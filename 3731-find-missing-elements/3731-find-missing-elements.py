class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minv=min(nums)
        maxv=max(nums)
        n=len(nums)
        ans=[]
        nums=set(nums)
        for i in range(maxv-minv+1):
            if (minv+i) not in nums:
                ans.append(minv+i)
        return ans