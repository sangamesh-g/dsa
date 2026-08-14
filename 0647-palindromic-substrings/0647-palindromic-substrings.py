class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            left=i
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                print(s[left],s[right],ans)
                ans+=1
                left-=1
                right+=1
            
            left_=i
            right_=i+1
            while left_>=0 and right_<n and s[left_]==s[right_]:
                print(s[left_],s[right_],ans)
                ans+=1
                left_-=1
                right_+=1
        
        return ans

# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         count = 0 

#         for i in range(len(s)):
#             count += self.func(i, i , s)
#             count += self.func(i, i+1 , s)
        
#         return count
    
#     @staticmethod
#     def func(left , right , s):
#         count = 0
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             count += 1
#             left -= 1
#             right += 1
        
#         return count