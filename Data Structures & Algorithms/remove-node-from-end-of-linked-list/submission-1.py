# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # create a gap of length n:
        for _ in range(n):
            right = right.next

        # point left where right "falls off"
        while right:
            right = right.next
            left = left.next

        # now we are in the right spot, right before nth from the end. remove:
        left.next = left.next.next

        return dummy.next