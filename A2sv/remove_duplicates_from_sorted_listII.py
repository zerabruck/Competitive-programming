# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        
        if not head or not head.next:
            return head
        start = dummy.next
        end = dummy.next.next
        prev = dummy
        while end:
            if start.val == end.val:
                while end and end.val == start.val:
                    end = end.next

                prev.next = end
                if not end:
                    break 
                start = prev

            prev = start
            start = start.next
            end = end.next

        return dummy.next        
