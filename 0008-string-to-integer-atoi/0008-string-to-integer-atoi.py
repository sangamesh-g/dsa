class Solution:
    max_val=2**31-1
    min_val=-2**31
    def myAtoi(self, s: str) -> int:
        neg=False
        i=0
        n=len(s)
        ans=0
        while i<n and s[i]==" ":
            i+=1

        if i<n and s[i]=='-':
            neg=True 
            i+=1
        
        elif i<n and s[i]=='+':
            i+=1
            if i>=n or not s[i].isdigit():  
                return 0

        limit = 2147483648 if neg else 2147483647

        while i<n and s[i].isdigit():
            ans*=10
            ans+=ord(s[i])-ord('0')
            if ans>=limit:
                ans=limit
                break
            i+=1
        
        return -ans if neg else ans