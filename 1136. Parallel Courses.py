'''You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.

In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous semester for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1.
Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.'''

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        incount=[0]*(n+1)
        print(incount)
        for s,e in relations:
            graph[s].append(e)
            incount[e]+=1
            
            
        queue=[]
        for node in graph:
            if incount[node]==0:
                queue.append(node)
                
        count=0
        steps=0
        while queue:
            steps+=1
            
            next_queue = []
            for node in queue:
                count += 1
                end_nodes = graph[node]
                for end_node in end_nodes:
                    incount[end_node] -= 1
                    if incount[end_node] == 0:
                        next_queue.append(end_node)
            queue = next_queue
            
        return steps if count == n else -1
