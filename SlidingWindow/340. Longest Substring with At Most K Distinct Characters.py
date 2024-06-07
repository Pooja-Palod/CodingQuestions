'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.'''

#sol1
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l=0
        m=defaultdict(int)
        ans=0
        for r in range(len(s)):
            m[s[r]]+=1
            while len(m)>k:
                m[s[l]]-=1
                if m[s[l]]==0:
                    del m[s[l]]
                l+=1
            ans=max(ans,r-l+1)
        return ans


#sol2
 def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_size = 0
        counter = Counter()
        
        for right in range(len(s)):
            counter[s[right]] += 1
            
            if len(counter) <= k:
                max_size += 1
            else:
                counter[s[right - max_size]] -= 1
                if counter[s[right - max_size]] == 0:
                    del counter[s[right - max_size]]
                    
        return max_size
        
