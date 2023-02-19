'''Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.''' 
 # Definition for a binary tree node.
 
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        def getHeight(node):
            if not node:
                return -1

            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            current_height = max(left_height, right_height) + 1

            if len(self.result) == current_height:
                self.result.append([])

            self.result[current_height].append(node.val)
            return current_height

        getHeight(root)
        return self.result

