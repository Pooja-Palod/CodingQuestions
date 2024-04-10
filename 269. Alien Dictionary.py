'''There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are sorted lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

 

Example 1:

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
Example 2:

Input: words = ["z","x"]
Output: "zx"
Example 3:

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of only lowercase English letters.'''


'''Approach 1 BFS (Kahn algorithm')'''

from collections import defaultdict, Counter, deque

def alienOrder(self, words: List[str]) -> str:
    
    # Step 0: create data structures + the in_degree of each unique letter to 0.
    adj_list = defaultdict(set)
    in_degree = Counter({c : 0 for word in words for c in word})
            
    # Step 1: We need to populate adj_list and in_degree.
    # For each pair of adjacent words...
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    in_degree[d] += 1
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): return ""
    
    # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
    output = []
    queue = deque([c for c in in_degree if in_degree[c] == 0])
    while queue:
        c = queue.popleft()
        output.append(c)
        for d in adj_list[c]:
            in_degree[d] -= 1
            if in_degree[d] == 0:
                queue.append(d)
                
    # If not all letters are in output, that means there was a cycle and so
    # no valid ordering. Return "" as per the problem description.
    if len(output) < len(in_degree):
        return ""
    # Otherwise, convert the ordering we found into a string and return it.
    return "".join(output)



'''Complexity Analysis

Let N be the total number of strings in the input list.
Let C be the total length of all the words in the input list, added together.
Let U be the total number of unique letters in the alien alphabet. While this is limited to 26
26 in the question description, we'll still look at how it would impact the complexity if it was not limited (as this could potentially be a follow-up question).

Time complexity :O(C).

There were three parts to the algorithm; identifying all the relations, putting them into an adjacency list, and then converting it into a valid alphabet ordering.
In the worst case, the first and second parts require checking every letter of every word (if the difference between two words was always in the last letter). 
O(C).

For the third part, recall that a breadth-first search has a cost of 
O(V+E), where 
V is the number of vertices and 
E is the number of edges. Our algorithm has the same cost as BFS, as it too is visiting each edge and node once (a node is visited once all of its edges are visited, unlike the traditional BFS where it is visited once one edge is visited). Therefore, determining the cost of our algorithm requires determining how many nodes and edges there are in the graph.

Nodes: We know that there is one vertex for each unique letter, i.e. O(U) vertices.
Edges: Each edge in the graph was generated from comparing two adjacent words in the input list. There are N−1 pairs of adjacent words, and only one edge can be generated from each pair. This might initially seem a bit surprising, so let's quickly look at an example. We'll use English words.
abacus
algorithm
the only conclusion we can draw is that b is before l. This is the reason abacus appears before algorithm in an English dictionary. The characters afterward are irrelevant. It is the same for the "alien" alphabets we're working with here. The only rule we can draw is the one based on the first difference between the two words.
Also, remember that we are only generating rules for adjacent words. We are not adding the "implied" rules to the adjacency list. For example, assume we have the following word list.

rgh
xcd
tny
bcd
We are only generating the following 3 edges.

r -> x
x -> t
t -> b
We are not generating these implied rules (the graph structure shows them indirectly).

r -> t
r -> b
x -> b
So with this, we know that there are at most N - 1 edges.

There is an additional upper limit on the number of edges too—it is impossible for there to be more than one edge between each pair of nodes. With 
U nodes, this means there can't be more than U^2 edges.

 we know it is at most the smallest of these two values. Mathematically, we can say this is 
min(U^2,N−1).

Going all the way back to the cost of breadth first search, we can now substiute in the number of nodes and the number of edges: 
V=U and 
E=min(U^2,N−1). This gives us:

O(V+E)=O(U+min(U^2,N−1))=

Finally, we need to combine the two parts: 
O(C) for the first and second parts, and O(U+min(U^2,N−1))
. When we have two independent parts, we add the costs together, as we don't necessarily know which is larger. After we've done this, we should look at the final formula and see whether or not we can actually draw any conclusions about which is larger. Adding them together, we initially get the following:

Space complexity
U is a constant fixed at a maximum of 26 O(1)
But when we consider an arbitrarily large number of possible letters, we use the size of the adjacency list
O(U+min(U^2,N)).'''

'''Approach 2'''

def alienOrder(self, words: List[str]) -> str:

    # Step 0: Put all unique letters into the adj list.
    reverse_adj_list = {c : [] for word in words for c in word}

    # Step 1: Find all edges and put them in reverse_adj_list.
    for first_word, second_word in zip(words, words[1:]):
        for c, d in zip(first_word, second_word):
            if c != d: 
                reverse_adj_list[d].append(c)
                break
        else: # Check that second word isn't a prefix of first word.
            if len(second_word) < len(first_word): 
                return ""

    # Step 2: Depth-first search.
    seen = {} # False = grey, True = black.
    output = []
    def visit(node):  # Return True iff there are no cycles.
        if node in seen:
            return seen[node] # If this node was grey (False), a cycle was detected.
        seen[node] = False # Mark node as grey.
        for next_node in reverse_adj_list[node]:
            result = visit(next_node)
            if not result: 
                return False # Cycle was detected lower down.
        seen[node] = True # Mark node as black.
        output.append(node)
        return True

    if not all(visit(node) for node in reverse_adj_list):
        return ""

    return "".join(output)


'''Approach 3''''
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj={c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                    
        output=[]
        visit={} #true-in current path #false
        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node]=True
            for char in adj[node]:
                if dfs(char):
                    return True
            visit[node]=False
            output.append(node)
            
        for c in adj:
            if dfs(c):
                return ""
            
        output.reverse()
        return "".join(output)

            
    

