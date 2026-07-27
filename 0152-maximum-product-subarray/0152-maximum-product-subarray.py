from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_end = nums[0]   # Maximum product ending here
        min_end = nums[0]   # Minimum product ending here
        ans = nums[0]

        for x in nums[1:]:

            # Negative number flips max and min
            if x < 0:
                max_end, min_end = min_end, max_end

            # Either start a new subarray or extend the previous one
            max_end = max(x, max_end * x)
            min_end = min(x, min_end * x)

            ans = max(ans, max_end)

        return ans