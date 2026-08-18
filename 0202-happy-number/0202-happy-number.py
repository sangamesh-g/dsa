class Solution:
    def isHappy(self, n: int) -> bool:
        if 1<n<=3:
            return False

        seen=set()
        
        while n>3:
            if n in seen:
                return False
            seen.add(n)
            ans=0
            for i in str(n):
                ans+=int(i)**2
            n=ans
        
        return True if n==1 else False
            