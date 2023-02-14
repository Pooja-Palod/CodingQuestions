
''' 
737 https://leetcode.com/problems/sentence-similarity-ii/We can represent a sentence as an array of words, for example, the sentence "I am happy with leetcode" can be represented as arr = ["I","am",happy","with","leetcode"].

Given two sentences sentence1 and sentence2 each represented as a string array and given an array of string pairs similarPairs where similarPairs[i] = [xi, yi] indicates that the two words xi and yi are similar.

Return true if sentence1 and sentence2 are similar, or false if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar.
Notice that a word is always similar to itself, also notice that the similarity relation is transitive. For example, if the words a and b are similar, and the words b and c are similar, then a and c are similar.

Input: sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
Output: true
Explanation: The two sentences have the same length and each word i of sentence1 is also similar to the corresponding word in sentence2.'''

from typing import List
import sys
import argparse

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
       
        if len(sentence1)!=len(sentence2):
            return False
        parent={}
        rank={}
        
        
        for similarPair in similarPairs:
            parent[similarPair[0]] = similarPair[0]
            parent[similarPair[1]] = similarPair[1]
            rank[similarPair[0]] = 1
            rank[similarPair[1]] = 1
        
        #path compression
        def find(n):
            res=n
            while res!=parent[res]:
                parent[res]=parent[parent[res]]
                res=parent[res]
            return res
        
        #union by rank
        def union(n1,n2):
            p1=find(n1)
            p2=find(n2)
            if p1!=p2:
                if rank[p1]>rank[p2]:
                    parent[p2]=p1
                elif rank[p1]<rank[p2]:
                    parent[p1]=p2
                else:
                    parent[p1]=p2
                    rank[p1]+=rank[p2]
            
            
        for similarPair in similarPairs:
           
            union(*similarPair)
      
        for i in range(len(sentence1)):
           
            if sentence1[i] == sentence2[i]:
                continue
            if not sentence1[i] in parent or not sentence2[i] in parent:
                return False
            if find(sentence1[i])!=find(sentence2[i]):
                return False
        return True



s=Solution()
parser=argparse.ArgumentParser()
parser.add_argument("--sentence1",nargs="*")
parser.add_argument("--sentence2",nargs="*")
parser.add_argument("--pairs",nargs="*")
args = parser.parse_args()
p=[]
for k in args.pairs:
  
   t=k.split(',')
  
   p.append([t[0][1:],t[1][:-1]])
#print(p)
print(s.areSentencesSimilarTwo(args.sentence1,args.sentence2,p))
      
        