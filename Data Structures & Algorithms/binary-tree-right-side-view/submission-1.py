# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        q = deque([(root, 0)])
        res = []

        while q:

            curr, lvl = q.popleft()

            if curr.right:
                q.append([curr.right, lvl + 1])
            if curr.left:
                q.append([curr.left, lvl + 1])

            if lvl >= len(res):
                res.append(curr.val)
            else:
                continue
        
        return res