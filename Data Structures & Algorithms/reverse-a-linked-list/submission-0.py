# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        current = head

        while current:
            nxt = current.next # save next
            current.next = prev # set to prev
            prev = current # set prev
            current = nxt # set current to new next

        return prev # prev becomes new head. 
