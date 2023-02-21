# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-6000,head)
        cur = dummy.next
        prev = dummy
        while cur:
            inner_prev = dummy
            inner_cur = head

            while inner_cur != cur:
                if inner_cur.val > cur.val:
                    break

                inner_prev = inner_cur
                inner_cur = inner_cur.next

            if inner_cur == cur:
                prev = cur
                cur = cur.next
                continue

            next_ele = cur.next
            # detach
            prev.next = cur.next
            cur.next = None

            # attach
            inner_prev.next = cur
            cur.next = inner_cur
            
            cur = next_ele
            head = dummy.next

        return head
        
