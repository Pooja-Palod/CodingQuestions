'''Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.
Input: root = [4,2,5,1,3], target = 3.714286
Output: 4'''

#Approach 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans=float('inf')
        diff=float('inf')
        
        def dfs(node):
            nonlocal ans
            nonlocal diff
            if not node:
                return
            if abs(node.val-target)<=diff:
                diff=abs(node.val-target)
                ans=node.val
                print(diff,ans)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ans
        
       
 #Approach 2:Inorder traversal
 
 class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r: TreeNode):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return min(inorder(root), key = lambda x: abs(target - x))
        
        
 #Approach 3:Iterative Inorder, O(k) time
 
 
 class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(target - x))
                
            pred = root.val
            root = root.right

        return pred

#Approach 4 Binary search

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
