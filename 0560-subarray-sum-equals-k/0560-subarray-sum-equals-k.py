class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=0
        cnt=0
        mp=defaultdict(int)
        mp[0]=1
        for i in nums:
            prefix+=i
            cnt+=mp[prefix-k]
            mp[prefix]+=1
        return cnt