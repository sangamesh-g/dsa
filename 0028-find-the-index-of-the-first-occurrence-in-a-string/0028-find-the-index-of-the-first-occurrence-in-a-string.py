class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # n=len(haystack)
        # m=len(needle)
        # i=0

        # haystack=haystack[::-1]
        # needle=needle[::-1]
        # while (n-i)>=m:
        #     if haystack.endswith(needle):
        #         return i
        #     i+=1
        #     haystack=haystack[:-1]
        
        # return -1
        
        return haystack.find(needle)