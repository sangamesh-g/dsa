class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowlen=len(matrix)
        collen=len(matrix[0])
        is_first_col_zero=False
        is_first_row_zero=False
        for i in range(collen):
            if matrix[0][i]==0:
                is_first_row_zero=True
        for j in range(rowlen):
            if matrix[j][0]==0:
                is_first_col_zero=True

        for i in range(1,rowlen):
            for j in range(1,collen):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(1, rowlen):
            for j in range(1, collen):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if is_first_row_zero:
            for k in range(collen):
                matrix[0][k]=0

        if is_first_col_zero:
            for k in range(rowlen):
                matrix[k][0]=0