class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        map=defaultdict(int)
        j=0
        while j<len(nums):
            map[nums[j]]+=1
            if map[nums[j]]>2:
                map[nums[j]]-=1
                del nums[j]
            else:
                j+=1
        return len(nums)