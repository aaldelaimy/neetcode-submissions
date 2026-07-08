# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque([(root, 0)])

        res = []

        while q:

            curr, lvl = q.popleft()

            if curr.left:
                q.append((curr.left, lvl + 1))
            if curr.right:
                q.append((curr.right, lvl + 1))

            if lvl < len(res):
                res[lvl].append(curr.val)
            else:
                res.append([curr.val])
        return res






