'''1102:https://leetcode.com/problems/path-with-maximum-minimum-value/
Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

The score of a path is the minimum value in that path.

For example, the score of the path 8 → 4 → 5 → 9 is 4.
Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: The path with the maximum score is highlighted in yellow. 
use BFS+priority queue(heap)
'''

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        heap=[(-grid[0][0],0,0)]
        visit=set((0,0))
        ans=grid[0][0]
        m=len(grid)
        n=len(grid[0])
        while heap:
            val,row,col=heapq.heappop(heap)
            ans=min(ans,-1*val)
            if row==m-1 and col==n-1:
                break
           
            for nr,nc in [(1,0),(-1,0),(0,1),(0,-1)]:
                newr=nr+row
                newc=nc+col
                if 0<=newr<m and 0<=newc<n:
                    if (newr,newc) not in visit:
                        heapq.heappush(heap,(-grid[newr][newc],newr,newc))
                        visit.add((newr,newc))
        
        return ans
      
     
    #solution2
    
    class UnionFind:
    def __init__(self,n):
        self.rank=[1]*n
        self.parent=[i for i in range(n)]
        
    def find(self,n1):
        res=n1
        while res!=self.parent[res]:
            self.parent[res]=self.parent[self.parent[res]]
            res=self.parent[res]
        return res
    
    def union(self,n1,n2):
        p1=self.find(n1)
        p2=self.find(n2)
        if p1==p2:
            return False
        if self.rank[p1]>=self.rank[p2]:
            self.parent[p2]=p1
            self.rank[p1]+=p2
        else:
            self.parent[p1]=p2
            self.rank[p2]+=self.rank[p1]
        return True
    
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
      
                    
        R, C = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        uf=UnionFind(R*C)
      
        
        visited = [[False]*C for _ in range(R)]
        
        vals = [(row, col) for row in range(R) for col in range(C)]
        vals.sort(key = lambda x: grid[x[0]][x[1]], reverse=True)
        
        
        for curr_row, curr_col in vals:
            curr_pos = curr_row*C + curr_col
            
            visited[curr_row][curr_col] = True
            for d_row, d_col in dirs:
                new_row = curr_row + d_row
                new_col = curr_col + d_col
                new_pos = new_row * C + new_col
                
                if 0 <= new_row < R and 0 <= new_col < C and visited[new_row][new_col]:
                    uf.union(curr_pos, new_pos)
                    
            if uf.find(0) == uf.find(R*C - 1):
                return grid[curr_row][curr_col]
            
        return -1
                
