class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # n=len(s)
        # for i in range(n//2):
        #     s[i],s[n-i-1]=s[n-i-1],s[i]

        l=0
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1