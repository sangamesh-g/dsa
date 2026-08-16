class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        ans=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        print(ans)

        return [x[0] for x in ans[:k]]