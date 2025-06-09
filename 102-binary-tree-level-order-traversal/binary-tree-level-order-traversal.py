# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque

        queue = deque([root])

        res = []

        while queue:
            new = []
            for _ in range(len(queue)):
                
                node = queue.popleft()

                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    new.append(node.val)

            if new:
                res.append(new)

        return res
