# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greater_head = greater = ListNode()
        lesser_head = lesser = ListNode()

        while head:
            if head.val >= x:
                greater.next = head
                greater = greater.next

            else:
                lesser.next = head
                lesser = lesser.next

            head = head.next
        greater.next = None
        lesser.next = greater_head.next
        lesser_head = lesser_head.next
        

        return lesser_head

