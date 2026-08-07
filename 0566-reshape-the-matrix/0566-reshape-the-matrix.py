class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        matrix=[num for nums in mat  for num in nums ]
        if len(matrix) != r * c:
            return mat
        
        ans=[[0]*c for _ in range(r)]
        k=0
        for i in range(r):
            for j in range(c):
                ans[i][j]=matrix[k]
                k+=1
        return ans
        