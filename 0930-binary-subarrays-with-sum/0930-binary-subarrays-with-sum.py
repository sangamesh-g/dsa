class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix=0
        sumdict={0:1}
        cnt=0
        for i in nums:
            prefix+=i
            cnt+=sumdict.get((prefix-goal),0)
            sumdict[prefix]=sumdict.get(prefix,0)+1
        return cnt