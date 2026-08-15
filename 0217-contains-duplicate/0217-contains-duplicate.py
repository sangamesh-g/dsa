class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # d={}
        # for i in nums:
        #     if i in d:
        #         return True
        #     d[i]=1
        # return False

        return len(set(nums))!=len(nums)

        # s=set()
        # for i in nums: