class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=len(s)
        n=ans
        for i in range(n):
            j=1
            while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
                print(s[i-j],s[i+j],ans)
                ans+=1
                j+=1
            
            j=i
            k=i+1
            while j>=0 and k<n and s[j]==s[k]:
                print(s[j],s[k],ans)
                ans+=1
                j-=1
                k+=1
        
        return ans