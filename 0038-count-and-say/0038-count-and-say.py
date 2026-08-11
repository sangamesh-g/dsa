class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'

        result=""
        count=1
        prev=self.countAndSay(n-1)
        print(prev)
        length=len(prev)
        for i in range(length):
            if i<length-1 and prev[i]==prev[i+1]:
                count+=1
            else:
                result+=str(count)+prev[i]
                count=1
        
        return result