class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = 0
        
        curr_max = 0
        global_max = nums[0]
        
        curr_min = 0
        global_min = nums[0]
        
        for num in nums:
            total_sum += num
            
            # Standard Kadane's for Maximum Subarray
            curr_max = max(num, curr_max + num)
            global_max = max(global_max, curr_max)
            
            # Inverted Kadane's for Minimum Subarray
            curr_min = min(num, curr_min + num)
            global_min = min(global_min, curr_min)
        
        # Edge Case: If all numbers are negative, global_max will be negative,
        # and total_sum - global_min will result in 0 (an empty subarray).
        # We must return global_max in this case because non-empty is required.
        if global_max < 0:
            return global_max
            
        return max(global_max, total_sum - global_min)