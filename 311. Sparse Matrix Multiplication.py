'''Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.

Example 1:

Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
Output: [[7,0,0],[-7,0,3]]
Example 2:

Input: mat1 = [[0]], mat2 = [[0]]
Output: [[0]]'''

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        def compress_matrix(matrix: List[List[int]]) -> List[List[int]]:
                rows, cols = len(matrix), len(matrix[0])
                compressed_matrix = [[] for _ in range(rows)]
                for row in range(rows):
                    for col in range(cols):
                        if matrix[row][col]:
                            compressed_matrix[row].append([matrix[row][col], col])
                return compressed_matrix
            
        
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        
        # Store the non-zero values of each matrix.
        A = compress_matrix(mat1)
        B = compress_matrix(mat2)
        
        ans = [[0] * n for _ in range(m)]
        
        for mat1_row in range(m):
            for element1,mat1_col in A[mat1_row]:
                for element2,mat2_col in B[mat1_col]:
                    ans[mat1_row][mat2_col]+=element1*element2
                    
        return ans
                    
