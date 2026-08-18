class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        n=len(nums)
        while i<n and j<n:
            if nums[i]%2==0:
                i+=2
                continue
            elif nums[j]%2!=0:
                j+=2
                continue
            else:
                nums[i],nums[j]=nums[j],nums[i]
                i+=2
                j+=2

        return nums