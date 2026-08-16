class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        n=len(nums)
        ans=0
        for i in nums:
            if i-1 not in nums:
                k=0
                current=i

                while current in nums:
                    current+=1
                    k+=1

                if ans<k:
                    ans=k
        
        return ans