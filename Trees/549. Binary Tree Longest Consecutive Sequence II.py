'''Given the root of a binary tree, return the length of the longest consecutive path in the tree.

A consecutive path is a path where the values of the consecutive nodes in the path differ by one. This path can be either increasing or decreasing.

For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid.
On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Input: root = [2,1,3]
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].

Input: root = [1,2,3]
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        res=0
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0,0
            
            inc,dec=1,1
            left_inc,left_dec=dfs(node.left)
            right_inc,right_dec=dfs(node.right)
            if node.left:
                if node.left.val==node.val+1:
                    inc = max(inc, 1 + left_inc)
                if node.left.val==node.val-1:
                    dec = max(dec, 1 + left_dec)
            if node.right:
                if node.right.val==node.val+1:
                    inc = max(inc, 1 + right_inc)
                if node.right.val==node.val-1:
                    dec = max(dec, 1 + right_dec)
            
            res=max(res,inc+dec-1)
            return (inc,dec)
        
        dfs(root)
        return res
                    
                    
                
            
                
                
