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

        res = []
        
        q = deque([(root, 0)])
        
        while q:

            curr, lvl = q.popleft()

            if len(res) == lvl:
                res.append(curr.val)
            
            if curr.right:
                q.append((curr.right, lvl + 1))
            if curr.left:
                q.append((curr.left, lvl + 1))
        
        return res