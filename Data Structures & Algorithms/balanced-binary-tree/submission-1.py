class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        
        def get_height(node): 
            if not node: 
                return 0 

            return 1 + max(get_height(node.left), get_height(node.right))

        left = get_height(root.left)
        right = get_height(root.right)

        if abs(left - right) > 1:
            return False 

        


        return self.isBalanced(root.left) and self.isBalanced(root.right)