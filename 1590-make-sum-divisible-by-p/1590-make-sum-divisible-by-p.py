class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        target=total%p
        if target==0:
            return 0
        
        pref={0:-1}
        ans=len(nums)
        prefix=0

        for i,num in enumerate(nums):
            prefix=(prefix+num)%p
            needed=(prefix-target)%p
            if needed in pref:
                a=i-pref[needed]
                if a<ans:
                    ans=a

            pref[prefix]=i

        return -1 if ans==len(nums) else ans
