class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        arr1=nums[n-k:]
        arr1.extend(nums[:n-k])
        nums[:]=arr1[:]