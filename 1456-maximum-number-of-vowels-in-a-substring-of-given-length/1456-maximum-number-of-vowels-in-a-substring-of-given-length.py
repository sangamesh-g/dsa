class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt=0
        vowels=set('aeiou')
        for j in range(k):
            if((s[j]) in vowels):
                cnt+=1
        maxv=cnt
        for i in range(len(s)-k):
            if((s[i]) in vowels):
                cnt-=1
            if((s[i+k] in vowels)):
                cnt+=1
            maxv=max(maxv,cnt)
        return maxv