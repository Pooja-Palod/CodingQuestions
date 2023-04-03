'''Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, 
return the shortest distance between these two words in the list.

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
'''

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1=-1
        p2=-1
        ans=len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1:
                p1=i
            elif wordsDict[i]==word2:
                p2=i
            if p1!=-1 and p2!=-1:
                ans=min(ans,abs(p1-p2))
        return ans
            
