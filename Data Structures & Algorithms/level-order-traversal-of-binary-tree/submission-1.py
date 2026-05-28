# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if root:
            queue = [(root, 0)]
        else:
            return []

        while queue:
            # queue = [,(4,2),(5,2)]
            # (3,1)
            curr, level = queue.pop(0)

            if len(res) <= level:
                res.append([])
            # res = [[1],[2,3]] 
            res[level].append(curr.val)

            if curr.left:
                queue.append((curr.left, level + 1))
            if curr.right: 
                queue.append((curr.right, level + 1))

        return res




