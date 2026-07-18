class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        for i in range(k):
            sum+=nums[i]
        avg=sum/k
        for i in range(len(nums)-k):
            sum-=nums[i]
            sum+=nums[i+k]
            if(sum/k>avg):
                avg=sum/k
        return avg
            
