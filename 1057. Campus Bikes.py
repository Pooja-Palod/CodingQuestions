'''On a campus represented on the X-Y plane, there are n workers and m bikes, with n <= m.

You are given an array workers of length n where workers[i] = [xi, yi] is the position of the ith worker. You are also given an array bikes of length m where bikes[j] = [xj, yj] is the position of the jth bike. All the given positions are unique.

Assign a bike to each worker. Among the available bikes and workers, we choose the (workeri, bikej) pair with the shortest Manhattan distance between each other and assign the bike to that worker.

If there are multiple (workeri, bikej) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index. If there are multiple ways to do that, we choose the pair with the smallest bike index. Repeat this process until there are no available workers.

Return an array answer of length n, where answer[i] is the index (0-indexed) of the bike that the ith worker is assigned to.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.
Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]
Explanation: Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].'''

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        def find_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])
        
        worker_to_bike_list = []
        pq = []
        
        for worker, worker_loc in enumerate(workers):
            curr_list=[]
            for bike, bike_loc in enumerate(bikes):
                distance =find_distance(worker_loc, bike_loc)
                curr_list.append((distance,worker, bike))
                
            curr_list.sort(reverse=True)
            heapq.heappush(pq, curr_list.pop())
            worker_to_bike_list.append(curr_list)
       
        
        bike_status = [False] * len(bikes)
        worker_status = [-1] * len(workers)
       
        while pq:
          
            distance, worker, bike = heapq.heappop(pq)
            if not bike_status[bike]:
                bike_status[bike] = True
                worker_status[worker] = bike
            else:
                next_closest_bike = worker_to_bike_list[worker].pop() 
                heapq.heappush(pq, next_closest_bike)
          
        return worker_status
