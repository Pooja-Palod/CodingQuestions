'''Given the root of a binary tree, find the largest subtree, which is also a Binary Search Tree (BST), where the largest means subtree has the largest number of nodes.

A Binary Search Tree (BST) is a tree in which all the nodes follow the below-mentioned properties:

The left subtree values are less than the value of their parent (root) node's value.
The right subtree values are greater than the value of their parent (root) node's value.
Note: A subtree must include all of its descendants.

Example 1:
Input: root = [10,5,15,1,8,null,7]
Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one. The return value is the subtree's size, which is 3.

Example 2:
Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
Output: 2'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        self.ans=0
        def dfs(root):
            if not root:
                return (0,float('inf'),float('-inf'))
            countleft,lowleft,highleft=dfs(root.left)
            countright,lowright,highright=dfs(root.right)
            
            nNodes=-1
            if countleft>-1 and countright>-1 and highleft<root.val<lowright:
                nNodes=countleft+countright+1
                self.ans=max(self.ans,nNodes)
            
            low=min(lowleft,root.val)
            high=max(highright,root.val)
            
            return (nNodes,low,high)
        
        
       
        dfs(root)
        return self.ans

 
