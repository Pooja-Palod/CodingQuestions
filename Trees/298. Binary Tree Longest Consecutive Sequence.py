'''https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

Given the root of a binary tree, return the length of the longest consecutive sequence path.

A consecutive sequence path is a path where the values increase by one along the path.

Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.
Input: root = [1,null,3,2,4,null,null,null,5]
Output: 3
Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

Input: root = [2,null,3,2,null,1]
Output: 2
Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.'''

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def longest_path(node):
            nonlocal res
            if not node:
                return 0
            length=1
            left=longest_path(node.left)
            right=longest_path(node.right)
            if node.left and node.left.val==node.val+1:
                length=max(length,left+1)
            if node.right and node.right.val==node.val+1:
                length=max(length,right+1)
            res=max(length,res)
            return length
              
        res=0
        longest_path(root)
        return res
    
