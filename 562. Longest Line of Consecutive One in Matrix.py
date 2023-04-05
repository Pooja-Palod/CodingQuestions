'''Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3'''
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if len(mat)==0:
            return 0
        dp=[[[0,0,0,0] for j in range(len(mat[0]))] for i in range(len(mat))]
        ans=0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1:
                    dp[i][j][0]=dp[i][j-1][0]+1 if j>0 else 1
                    dp[i][j][1]=dp[i-1][j][1]+1 if i>0 else 1
                    dp[i][j][2]=dp[i-1][j-1][2]+1 if i>0 and j>0  else 1
                    dp[i][j][3]=dp[i-1][j+1][3]+1 if i>0 and j<len(mat[0])-1  else 1
                ans=max(ans,dp[i][j][0],dp[i][j][1],dp[i][j][2],dp[i][j][3])
        return ans
