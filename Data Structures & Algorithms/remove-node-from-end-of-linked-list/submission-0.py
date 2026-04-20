# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        target = length - n
        
        counter = 0
        temp = head
        if target > 0:
            while temp:
                counter += 1
                if counter == target:
                    temp.next = temp.next.next
                    break

                temp = temp.next
        else:
            return head.next

        return head