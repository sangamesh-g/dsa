class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        sumdict={0:1}
        cnt=0
        for i in nums:
            prefix+=i
            cnt+=sumdict.get((prefix)%k,0)
            sumdict[prefix%k]=sumdict.get((prefix%k),0)+1
        return cnt