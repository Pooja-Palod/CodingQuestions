'''Given a string s and an integer k, return the number of substrings in s of length k with no repeated character
Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
'''

class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        m=defaultdict(int)
        ans=0
        l=0
        for r in range(len(s)):
            m[s[r]]+=1
            
            while m[s[r]]>1:
                m[s[l]]-=1
                l+=1
                
            if (r-l+1)==k:
                ans+=1
                m[s[l]]-=1
                l+=1
        return ans
                
