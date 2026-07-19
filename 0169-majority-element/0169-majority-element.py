class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj=len(nums)/2
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
            if freq[nums[i]]>=maj:
                return nums[i]