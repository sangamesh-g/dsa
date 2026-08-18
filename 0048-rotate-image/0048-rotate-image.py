class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        print([list(row) for row in zip(matrix)])
        matrix[:]=[row[::-1] for row in zip(*matrix)]