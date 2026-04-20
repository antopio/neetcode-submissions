# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q:
            p_queue = deque([p])
            q_queue = deque([q])
        else:
            return False

        while p_queue and q_queue:
            len_p = len(p_queue)
            len_q = len(q_queue)
            if len_p != len_q:
                return False
            for _ in range(len_p):
                curr_p = p_queue.popleft()
                curr_q = q_queue.popleft()

                if curr_p.val != curr_q.val:
                    return False

                if curr_p.left and curr_q.left:
                    p_queue.append(curr_p.left)
                    q_queue.append(curr_q.left)

                elif curr_p.left and not curr_q.left or not curr_p.left and curr_q.left:
                    return False
                
            
                if curr_p.right and curr_q.right:
                    p_queue.append(curr_p.right)
                    q_queue.append(curr_q.right)

                elif curr_p.right and not curr_q.right or not curr_p.right and curr_q.right:
                    return False
            
        
        return True