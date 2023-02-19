# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-200,head)
        prev = dummy
        curr = dummy.next
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next

            else:
                prev = curr

            curr = curr.next

        return dummy.next
       
