class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans=0
        prefix=0
        prefdict={0:-1}
        for i,num in enumerate(nums):
            prefix+=-1 if num==0 else +1
            # print(prefix)
            if prefix in prefdict:
                if ans<i-prefdict[prefix]:
                    ans=i-prefdict[prefix]
            else:
                prefdict[prefix]=i
        
        return ans