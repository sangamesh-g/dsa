class Solution:
    # def palin(self,s:str):
    #     left=0
    #     right=len(s)-1
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True

    # def shortestPalindrome(self, s: str) -> str:
        
    #     n=len(s)
    #     r=n-1
    #     while r>=0:
    #         if self.palin(s[:r+1]):
    #             break
    #         r-=1
    #     sufix=s[r+1:]
    #     return sufix[::-1]+s

    def shortestPalindrome(self, s: str) -> str:
        rev=s[::-1]
        n=len(s)
        r=0
        for r in range(n):
            if s[:n-r]==rev[r:]:
                return rev[:r]+s
        return ""
        