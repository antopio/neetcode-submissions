# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # empty? bail
        if not root:
            return []

        # put the root node in line
        queue = deque([root])
        result = []
        # outer loop, run while we have nodes
        while queue:
            # get the size of this level:
            level_size = len(queue)
            temp = []
            #process current level's nodes:
            for _ in range(level_size):
                # "serve the first customer in line"
                current = queue.popleft()
                
                # my logic:
                temp.append(current.val)

                # end logic:

                #put children into the queue:
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            result.append(temp)

        return result


            
            

        