# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = deque([root])

        while queue:
            len_root = len(queue)
            for _ in range(len_root):
                node = queue.popleft()
                if node.val == subRoot.val:
                    if self.isSameTree(node, subRoot):
                        return True
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return False
                
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q or p.val!=q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)