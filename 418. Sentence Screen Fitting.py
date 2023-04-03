'''Given a rows x cols screen and a sentence represented as a list of strings, return the number of times the given sentence can be fitted on the screen.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words in a line.

Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.

Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd- 
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.

Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.
'''
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        memo={}
        n=len(sentence)
        def dfs(i):
            if i in memo:
                return memo[i]
            c=0
            index=i
            times=0
            while c+len(sentence[i])<=cols:
                c+=len(sentence[i])+1
                i+=1
                if i==n:
                    times+=1
                    i=0
            memo[index]=[i,times]
            return memo[index]
        
        
        
        ans=0
        idx=0
        
        for _ in range(rows):
            res=dfs(idx)
            ans+=res[1]
            idx=res[0]
            
        return ans
            
 
