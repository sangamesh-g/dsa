class Solution:
    def reverse(self, x: int) -> int:
        n=abs(x)
        ans=0
        while(n>0):
            ans=ans*10+n%10
            n//=10
        if ans > 2**31 - 1:
            return 0
        return ans if x>0 else -ans