class Solution:
    def countAndSay(self, n: int) -> str:
        
        prev='1'
        for _ in range(n-1):
            result=''
            count=1
            length=len(prev)
            for i in range(length):
                if i<length-1 and prev[i]==prev[i+1]:
                    count+=1
                else:
                    result+=str(count)+prev[i]
                    count=1
            prev=result
            
        return prev