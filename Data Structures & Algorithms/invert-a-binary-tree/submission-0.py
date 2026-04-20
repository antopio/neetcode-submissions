# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            len_nodes = len(queue)
            for _ in range(len_nodes):
                node = queue.popleft()
                right = node.right
                left = node.left
                node.right = left
                node.left = right

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root




        



        