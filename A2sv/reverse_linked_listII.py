# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = dummy
        for i in range(left - 1):
            curr = curr.next
        left_prev = curr
        prev = None
        curr = curr.next
        difference = (right - left) + 1
        for i in range(difference ):
            right_next = curr.next
            curr.next = prev
            prev = curr
            curr = right_next             
        left = left_prev.next
        left.next = curr
        left_prev.next = prev
        return dummy.next
