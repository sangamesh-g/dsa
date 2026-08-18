class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums=set(nums)
        n=len(nums)
        ans=1
        for i in nums:
            if i-1 not in nums:
                
                l=1

                while i+l in nums:
                    l+=1

                if ans<l:
                    ans=l
        
        return ans