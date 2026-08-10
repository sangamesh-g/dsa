class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s is None:
            return -1
        
        n=len(s)
        count=Counter(s)
        for i in range(n):
            if count[s[i]]==1:
                return i

        return -1
        