class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max=sum(nums[:k])
        avgsum=max
        for i in range(len(nums)-k):
            avgsum-=nums[i]
            avgsum+=nums[i+k]
            if(avgsum>max):
                max=avgsum
        return max/k
            
