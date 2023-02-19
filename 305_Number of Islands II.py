'''You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 nput: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.'''


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent={}
        rank={}
        #path compression
        def find(n):
            res=n
            while  res !=parent[res]:
                parent[res]=parent[parent[res]]
                res=parent[res]
            return res
        
        #union by rank
        def union(n1,n2):
            p1=find(n1)
            p2=find(n2)
            if p1==p2:
                return False
            else:
                if rank[p1]>rank[p2]:
                    parent[p2]=p1
                elif rank[p1]<rank[p2]:
                    parent[p1]=p2
                else:
                    parent[p1]=p2
                    rank[p1]+=rank[p2]
                return True
           
        
        count=0
        seen=set()
        ans=[]
        for x,y in positions:
            if (x,y) not in seen:
                    seen.add((x,y))
                    parent[(x,y)]=(x,y)
                    rank[(x,y)]=1
                    count+=1
                    for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                            if (i,j) in seen and union((i,j),(x,y)):
                                count-=1
            ans.append(count)
        return ans
