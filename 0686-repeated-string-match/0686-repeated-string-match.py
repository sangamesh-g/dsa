class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        n=len(b)//len(a)
        # print(n)
        x=""
        for i in range(1,n+3):
            x+=a
            # print(x,b)
            if b in x:
                # print(ai)
                return i
        return -1