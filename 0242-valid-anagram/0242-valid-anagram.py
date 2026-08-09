class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreq={}
        tfreq={}
        for i in s:
            sfreq[i]=sfreq.get(i,0)+1
        for j in t:
            tfreq[j]=tfreq.get(j,0)+1
        return True if sfreq==tfreq else False