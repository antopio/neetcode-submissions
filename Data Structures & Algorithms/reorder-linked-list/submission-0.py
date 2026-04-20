# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half:
        second = slow.next # slow is at midpoint. 2nd half is at slow.next
        slow.next = None # break connection to second

        prev = None
        while second:
            temp = second.next # secure next vine
            second.next = prev # swing back
            prev = second # move camera
            second = temp # swing forward

        # merge two halves:
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        