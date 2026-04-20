# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # dummy
        dummy = ListNode(0)
        curr = dummy

        # make a heap
        heap = []

        # populate our heap:
        for i, list_node in enumerate(lists):
            heapq.heappush(heap, (list_node.val, i, list_node)) # push to heap with the first val, the position in lists and the node itself

        # loop, pop and replenish
        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node # set our node
            curr = curr.next # move over

            # if node has a next, add it:

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
            
        return dummy.next