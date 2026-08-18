class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        # print(dic)
        ans=sorted(dic,key=lambda x:dic[x],reverse=True)
        return ans[:k]