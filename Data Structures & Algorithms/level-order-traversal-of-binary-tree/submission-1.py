# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        queue.append(root)
        res = []

        while queue: 
            output = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node:
                    output.append(node.val) 
                    queue.append(node.left)
                    queue.append(node.right)

            if output:
                res.append(output)
        

        return res



