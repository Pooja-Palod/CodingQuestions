'''A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [ai, bi] represents the interval [ai, bi). You are also given another interval toBeRemoved.

Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
'''
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans=[]
        for start,end in intervals:
            if start>toBeRemoved[1] or end < toBeRemoved[0]:
                ans.append([start,end])
            else: 
                if start<toBeRemoved[0] :
                    ans.append([start,toBeRemoved[0]])
                if end>toBeRemoved[1]:
                    ans.append([toBeRemoved[1],end])
        return ans
            
            
            
                
                
