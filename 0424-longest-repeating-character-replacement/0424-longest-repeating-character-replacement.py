class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        freq={}
        maxfreq=0
        ans=0
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
            maxfreq=max(maxfreq,freq[s[i]])
            while(i-left+1-maxfreq>k):
                freq[s[left]]-=1
                left+=1
            ans=max(ans,i-left+1)
        return ans