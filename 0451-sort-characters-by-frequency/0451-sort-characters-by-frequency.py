class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        # sorted_count=sorted(count.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for x,y in count.most_common():
            ans+=x*y
        return ans