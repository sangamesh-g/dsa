class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=len(num1)-1
        j=len(num2)-1

        results=[]
        carry=0

        while i>=0 or j>=0 or carry:
            x=ord(num1[i])-ord('0') if i>=0 else 0
            y=ord(num2[j])-ord('0') if j>=0 else 0

            total=x+y+carry

            carry=total//10
            results.append(chr(ord('0')+total%10))
            i-=1
            j-=1

        return "".join(reversed(results))
