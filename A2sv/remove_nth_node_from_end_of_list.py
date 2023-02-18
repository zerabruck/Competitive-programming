# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev = dummy
        fast = dummy.next
        slow = dummy.next
        for i in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        prev.next = slow.next
        return dummy.next
