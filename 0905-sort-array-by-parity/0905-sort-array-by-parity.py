class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        while l<r:
            if nums[l]%2!=0:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
                continue
            l+=1
        return nums