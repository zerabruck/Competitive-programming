# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next
        start = even

        while even and even.next :
            save = even.next
            even.next = even.next.next
            odd.next = save
            even = even.next
            odd = odd.next

        if not even:
            odd.next = None

        odd.next = start
        return head
