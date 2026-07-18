class Solution:
    def isvowel(self,ch):
        return ch.lower()=='a'or ch.lower()=='e'or ch.lower()=='i' or ch.lower()=='o' or ch.lower()=='u'
    def maxVowels(self, s: str, k: int) -> int:
        cnt=0

        for j in range(k):
            if(self.isvowel(s[j])):
                cnt+=1
        maxv=cnt
        for i in range(len(s)-k):
            if(self.isvowel(s[i])):
                cnt-=1
            if(self.isvowel(s[i+k])):
                cnt+=1
            maxv=max(maxv,cnt)
        return maxv