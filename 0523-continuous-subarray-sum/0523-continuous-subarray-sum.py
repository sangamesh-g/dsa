class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:      
        prefix=0
        prefdict={0:-1}
        for i,num in enumerate(nums):
            prefix+=num
            rem=prefix%k
            if rem in prefdict:
                if i-prefdict[rem]>=2:
                    return True
            else:
                prefdict[rem] = i
        return False
