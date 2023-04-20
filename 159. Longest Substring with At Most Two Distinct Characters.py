'''Given a string s, return the length of the longest substring that contains at most two distinct characters.

 

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l=0
        r=0
        n=len(s)
        m={}
        distinct=0
        ans=0
        while r<n:
          
            if s[r] not in m:
                 distinct+=1
            m[s[r]]=m.get(s[r],0)+1
            
            #contract window 
            while distinct>2:
                    m[s[l]]-=1
                   
                    if m[s[l]]==0:
                        distinct-=1
                        del m[s[l]]
                    l+=1
            ans=max(ans,r-l+1)
            r+=1
           
         return ans
