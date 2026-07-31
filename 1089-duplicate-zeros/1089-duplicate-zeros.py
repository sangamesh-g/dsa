class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        length=len(arr)
        nums=[]
        for n in arr:
            if length<=i:
                break
            if length>i:
                nums.append(n)
                i+=1
                if length>i and n==0:
                    nums.append(0)
                    i+=1
        arr[:]=nums