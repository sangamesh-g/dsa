class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        k=0
        n=len(nums)
        while k<n:
            if k%2!=0:
                if nums[k]%2==0:
                    nums[i],nums[k]=nums[k],nums[i]
                    i+=2
                else:
                    k+=1
            elif k%2==0:
                if nums[k]%2!=0:
                    nums[j],nums[k]=nums[k],nums[j]
                    j+=2
                else:
                    k+=1
                    
        return nums