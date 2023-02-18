# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        first_dummy = ListNode(0,list1)
        second_dummy = ListNode(0,list2)
        prev = first_dummy
        first_cur = first_dummy.next
        sec_cur = second_dummy.next

        while first_cur and sec_cur:
            if first_cur.val <= sec_cur.val:
                prev.next = first_cur
                prev = first_cur
                first_cur = first_cur.next

            else:
                prev.next = sec_cur
                prev = sec_cur
                sec_cur = sec_cur.next
        if first_cur:
            prev.next = first_cur
        elif sec_cur:
            prev.next = sec_cur

        head = first_dummy.next
        return head
