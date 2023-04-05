We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. 
For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  
Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.'''

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap=[]
        for i,emp in enumerate(schedule):
            heapq.heappush(heap,(emp[0].start,i,0))
        
        heapq.heapify(heap)
        res = []
        _, i, j = heap[0]
        prev_end = schedule[i][j].end
        
        while heap:
            _, i, j =heapq.heappop(heap)
            if j + 1 < len(schedule[i]):
                heapq.heappush(heap, (schedule[i][j + 1].start, i, j + 1))
            interval=schedule[i][j]
            if interval.start>prev_end:
                res.append(Interval(prev_end,interval.start))
            prev_end=max(prev_end,interval.end)
            
        return res
                
