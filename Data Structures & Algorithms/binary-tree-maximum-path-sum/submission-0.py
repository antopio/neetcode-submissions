# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0

            left_straight = max(0, dfs(node.left))
            right_straight = max(0, dfs(node.right))

            current_arch = left_straight + node.val + right_straight

            self.max_sum = max(self.max_sum, current_arch)

            return node.val + max(left_straight, right_straight)
        
        dfs(root)

        return self.max_sum