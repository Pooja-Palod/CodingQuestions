'''317. Shortest Distance from All Buildings

You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.
Example 2:

Input: grid = [[1,0]]
Output: 1
Example 3:

Input: grid = [[1]]
Output: -1'''

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        Algorithm:
        1.For each grid[i][j] that is equal to 1, start a BFS. During the BFS:
            All 4-directionally adjacent grid cells with values equal to emptyLandValue are valid.
            Visit them one by one and store the distances of these cells from the source in a total matrix.
            Decrease the value of visited cells by 1.
        2.After each BFS traversal, decrement emptyLandValue by 1.
        3.Before we start a BFS call for a house, we set minDist equal to INT_MAX.
        4.Then we will traverse all of the empty land cells with values equal to emptyLandValue
        5.After the last BFS traversal, if the minimum distance equals INT_MAX, then there has not been any cell that can be reached by all the houses, so return -1.
        6.Otherwise, return the minimum distance minDist.
        
        
        """
        m=len(grid)
        
        n=len(grid[0])
        dist=[[0 for j in range(n)] for i in range(m)]
        building=1
        obstacle=2
        empty=0
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        mindist=float('inf')
        for row in range(m):
            for col in range(n):
                if grid[row][col]==building:
                    mindist=float('inf')
                    queue=deque([(row,col,0)])
                   
                    while queue:
                        r,c,d=queue.popleft()
                        for dr,dc in directions:
                            nextr=r+dr
                            nextc=c+dc
                            
                            if 0<=nextr<m and 0<=nextc<n and grid[nextr][nextc]==empty:
                                grid[nextr][nextc]-=1
                                queue.append((nextr,nextc,d+1))
                                dist[nextr][nextc]+=d+1
                                mindist=min(mindist, dist[nextr][nextc])
                    if mindist==float('inf'):
                        return -1
                    empty-=1
                           
                
        return mindist if mindist!=float('inf') else -1
                
        
 
