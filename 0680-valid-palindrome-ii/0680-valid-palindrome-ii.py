class Solution:

    def palin(self,l,r,s):
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return self.palin(l+1,r,s) or self.palin(l,r-1,s)
            l+=1
            r-=1
        return True