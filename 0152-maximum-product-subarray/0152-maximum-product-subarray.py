from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxend=nums[0]
        minend=nums[0]
        ans=nums[0]

        for n in nums[1:]:
            if n<0:
                maxend,minend=minend,maxend
            
            maxend=maxend*n if maxend*n>n else n
            minend=minend*n if minend*n<n else n
            if ans<maxend:
                ans=maxend
        return ans