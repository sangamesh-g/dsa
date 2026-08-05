class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # minv=min(nums)
        # maxv=max(nums)
        # n=len(nums)
        # ans=[]
        # nums=set(nums)
        # for i in range(maxv-minv+1):
        #     if (minv+i) not in nums:
        #         ans.append(minv+i)
        # return ans

        nums.sort()
        mi=nums[0]
        ma=nums[-1]
        i=0
        ans=[]
        while ma>mi:
            if mi==nums[i]:
                mi+=1
                i+=1
            else:
                ans.append(mi)
                mi+=1
        return ans