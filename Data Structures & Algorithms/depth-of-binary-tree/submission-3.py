# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        stack = [(root, 1)]
        res = 1

        while stack:

            curr, lvl = stack.pop()

            if lvl > res:
                res = lvl
            
            if curr.left:
                stack.append((curr.left, lvl + 1))
            if curr.right:
                stack.append((curr.right, lvl + 1))

        return res