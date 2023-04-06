'''A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. 
If the task is impossible, return -1.

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.'''


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sourceset=set(source)
        for char in target:
            if char not in sourceset:
                return -1
         
        sourceindex=0
        sourcelength=len(source)
        count=0
        for char in target:
            
             
            if sourceindex==0:
                    count+=1
                    
            while source[sourceindex]!=char:
                sourceindex=(sourceindex+1)% sourcelength
                
                if sourceindex==0:
                    count+=1
                    
            sourceindex=(sourceindex+1)% sourcelength
            
        return count
            
            
            
            
