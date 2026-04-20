# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: parent node first, left, right
        # inorder: left, up, right

        if not preorder or not inorder:
            return None
        
        # 1. The Anchor: The first item in preorder is ALWAYS the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # 2. The Split: Find where the root is in the inorder list
        # This index tells us exactly how many nodes are in the left subtree
        mid = inorder.index(root_val)
        
        # 3. Shrink and Repeat: Slice the arrays and recurse
        # Left Subtree:
        # - preorder: start after the root (index 1) and take 'mid' number of elements
        # - inorder: take everything up to 'mid'
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # Right Subtree:
        # - preorder: take everything after the left subtree's elements
        # - inorder: take everything after the root's index
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        return root

