# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # default case (found a leaf)
        if not root:
            return None

        if key == root.val:
            # check for children
            if not root.left and not root.right:
                return None
            elif root.right and not root.left:
                return root.right
            elif root.left and not root.right:
                return root.left
            else:
                # 1. Find the replacement value (minimum of the right subtree)
                root.val = self.get_min(root.right)
                # 2. Delete the duplicate node from the right subtree
                root.right = self.deleteNode(root.right, root.val)


        if key > root.val:
            # go right
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            # go left
            root.left = self.deleteNode(root.left, key)

        return root
        
    def get_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current.val