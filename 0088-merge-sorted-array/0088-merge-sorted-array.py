class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num=nums1[:m]
        nums2=nums2[:n]
        i=j=k=0
        while(k<=(m+n-1)):
            if j<=(n-1) and i<=(m-1) and num[i]>=nums2[j]:
                nums1[k]=nums2[j]
                j+=1
                k+=1
            elif i<=(m-1) and j<=(n-1) and num[i]<=nums2[j]:
                nums1[k]=num[i]
                k+=1
                i+=1
            elif i>=m or j>=n:
                if i>=m:
                    for x in nums2[j:]:
                        nums1[k]=x
                        k+=1
                if j>=n:
                    for y in num[i:]:
                        nums1[k]=y
                        k+=1
                break
