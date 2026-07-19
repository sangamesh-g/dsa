class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        window=set()
        ans=0
        maxlen=0
        for i in range(len(s)):
            while(s[i] in window):
                window.remove(s[left])
                left+=1
                ans-=1
            
            if s[i] not in window:
                window.add(s[i])
                ans+=1
            maxlen=max(ans,maxlen)

        return maxlen
