There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
Return the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
Example 2:

Input: costs = [[1,3],[2,4]]
Output: 5
 
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        #time complexity O(nk)
        housecount=len(costs)
        colors=len(costs[0])
        
        prev=costs[0]
        for i in range(1,housecount):
                curr_row=costs[i]
                mincolor=min(prev)
                minindex=prev.index(mincolor)
                secondmincolor=min(prev[:minindex]+prev[minindex+1:])
                
                for j in range(colors):
                    curr_row[j]+=mincolor if j!=minindex else secondmincolor
                prev=curr_row
            
                    
        return min(prev)
                
