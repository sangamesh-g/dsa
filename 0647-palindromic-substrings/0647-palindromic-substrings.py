# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         ans=len(s)
#         n=ans
#         for i in range(n):
#             j=1
#             while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
#                 print(s[i-j],s[i+j],ans)
#                 ans+=1
#                 j+=1
            
#             j=i
#             k=i+1
#             while j>=0 and k<n and s[j]==s[k]:
#                 print(s[j],s[k],ans)
#                 ans+=1
#                 j-=1
#                 k+=1
        
#         return ans

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 

        for i in range(len(s)):
            count += self.func(i, i , s)
            count += self.func(i, i+1 , s)
        
        return count
    
    @staticmethod
    def func(left , right , s):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        return count