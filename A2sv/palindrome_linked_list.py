# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first_dummy = ListNode()
        first_curr = first_dummy
        curr = head
        while(curr):
            new = ListNode(curr.val,first_curr)
            first_curr = new
            curr = curr.next  
        cur = head
        while(cur):
            if (cur.val != first_curr.val):
                return False

            first_curr = first_curr.next
            cur = cur.next

        return True
