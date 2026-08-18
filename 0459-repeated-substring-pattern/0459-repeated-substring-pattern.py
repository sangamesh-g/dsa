class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s=="":
            return False
        n=len(s)
        for i in range(1,n):
            if n%i!=0:
                continue
            
            r=n//i
            p=s[:i]
            if p*r==s:
                return True
        return False

