class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=s[0]
        al=1
        n=len(s)
        for i in range(n):
            j=1
            while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
                if len(s[i-j:i+j+1])>al:
                    ans=s[i-j:i+j+1]
                    al=len(ans)
                j+=1

            k=i
            l=i+1
            while k>=0 and l<n and s[k]==s[l]:
                if len(s[k:l])+1>al:
                    ans=s[k:l+1]
                    al=len(ans)
                k-=1
                l+=1
        return ans


        