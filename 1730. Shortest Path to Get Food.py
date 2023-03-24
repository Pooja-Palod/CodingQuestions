'''You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

You are given an m x n character matrix, grid, of these different types of cells:

'*' is your location. There is exactly one '*' cell.
'#' is a food cell. There may be multiple food cells.
'O' is free space, and you can travel through these cells.
'X' is an obstacle, and you cannot travel through these cells.
You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1

Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.'''


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        print(m,n)
        queue=deque()
        visit=set() 
        # find position of * in grid
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='*':
                    visit.add((i,j))
                    queue.append((i,j,0))
                    break       
        dire=[(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue:
                x,y,step=queue.popleft()
                if grid[x][y]=="#":
                    return step
                for dx,dy in dire:
                    newx=x+dx
                    newy=y+dy
                    if not (0<=newx<m and 0<=newy<n ):
                        continue
                    if  grid[newx][newy] in ("#","O") and (newx,newy) not in visit:
                            queue.append((newx,newy,step+1))
                            visit.add((newx,newy))
        return -1
            

