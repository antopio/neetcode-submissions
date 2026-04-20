# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # if tree empty, stop
        if not root:
            return []

        # init w/ root
        queue = deque([root])
        result = []
        # outer loop
        while queue:
            len_queue = len(queue)

            for i in range(len_queue):
                current = queue.popleft()
                if i+1 == len_queue:
                    result.append(current.val)
                # add children
                ### ORDER MATTERS!!!!!!!!!
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
            ## just add the last known current.val per level
            
        
        return result

        