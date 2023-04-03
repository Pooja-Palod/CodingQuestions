'''Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between the occurrence of these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
'''

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        prev=-1
        ans=len(wordsDict)
        for i in range(len(wordsDict)):
            if wordsDict[i]==word1 or  wordsDict[i]==word2:
                print("here")
                if prev!=-1 and (wordsDict[prev]!=wordsDict[i] or word1==word2):
                    ans=min(ans,i-prev)
                prev=i
                    
        return ans
            
