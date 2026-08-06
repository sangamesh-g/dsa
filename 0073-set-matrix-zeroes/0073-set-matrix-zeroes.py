class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowlen=len(matrix)
        rows=[False]*rowlen
        collen=len(matrix[0])
        cols=[False]*collen
        for i in range(rowlen):
            for j in range(collen):
                if matrix[i][j]==0:
                    rows[i]=True
                    cols[j]=True

        for i in range(rowlen):
            if rows[i]==True:
                for k in range(collen):
                    matrix[i][k]=0

        for j in range(collen):
            if cols[j]==True:
                for k in range(rowlen):
                    matrix[k][j]=0