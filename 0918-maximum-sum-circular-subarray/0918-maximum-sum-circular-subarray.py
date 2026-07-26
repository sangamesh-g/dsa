class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = 0
        
        curr_max = 0
        global_max = nums[0]
        
        curr_min = 0
        global_min = nums[0]
        
        for num in nums:
            total_sum+=num

            curr_max=curr_max+num if curr_max>0 else num
            if curr_max>global_max:
                global_max=curr_max
            
            curr_min=curr_min+num if curr_min+num<num else num
            if curr_min<global_min:
                global_min=curr_min
            
        if global_max<0:
            return global_max

        return max(global_max,total_sum-global_min)