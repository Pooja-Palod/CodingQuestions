'''There are n people in a social group labeled from 0 to n - 1. You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.
Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation: 
The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.'''
class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[1]*n
                 
    def find(self,n):
                res=n
                while res!=self.parent[res]:
                    self.parent[res]=self.parent[self.parent[res]]
                    res=self.parent[res]
                return res
    def union(self,n1,n2):
                p1=self.find(n1)
                p2=self.find(n2)
                if p1==p2:
                    return False
                if p1!=p2:
                    if self.rank[p1]<self.rank[p2]:
                        self.parent[p1]=p2
                    elif self.rank[p1]>self.rank[p2]:
                        self.parent[p2]=p1
                    else:
                        self.parent[p2]=p1
                        self.rank[p1]+=self.rank[p2]
                return True
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf=UnionFind(n)
        logs.sort()
        ans=0
        c=n
        for t,s,e in logs:
            if uf.union(s,e):
                c-=1
                ans+=1
                if c==1:
                    return t
        return -1
            
