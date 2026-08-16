class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        ans=dic.most_common(k)

        return [x[0] for x in ans]