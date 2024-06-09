'''
https://leetcode.com/problems/closest-binary-search-tree-value-ii/
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]
Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]'''

class Solution:
#O(n)
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        #
        queue=deque()
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            queue.append(node.val)
            if len(queue)>k:
                if abs(target-queue[0])<abs(target-queue[-1]):
                    queue.pop()
                else:
                    queue.popleft()
           
            dfs(node.right)
          
        dfs(root)
        return list(queue)


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def dfs(node, arr):
            if not node:
                return
            
            dfs(node.left, arr)
            arr.append(node.val)
            dfs(node.right, arr)
        
        arr = []
        dfs(root, arr)
        
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            if abs(target - arr[mid + k]) < abs(target - arr[mid]):
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
