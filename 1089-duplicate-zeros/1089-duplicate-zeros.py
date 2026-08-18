class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        nums=[]
        for n in arr:
            if len(nums)>=len(arr):
                break
            nums.append(n)
            if n==0:
                nums.append(0)
        arr[:]=nums[:len(arr)]