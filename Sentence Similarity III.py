''''1813. Sentence Similarity III
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.

Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.

Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true
Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".'''

import sys
from collections import deque 
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1, s2 = deque(sentence1.split()), deque(sentence2.split())
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        while s1 and s1[0] == s2[0]:
            s1.popleft()
            s2.popleft()
        while s1 and s1[-1] == s2[-1]:
            s1.pop()
            s2.pop()
        return not s1


s=Solution()
print(s.areSentencesSimilar(sys.argv[1],sys.argv[2]))