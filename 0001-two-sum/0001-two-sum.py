class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(n):
            j=target-nums[i]
            k=i+1
            while k<n:
                if nums[k]==j:
                    return [i,k]
                k+=1