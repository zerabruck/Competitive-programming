# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        max_sum = 0
        #find middle
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        #reverse from middle
        prev = None
        curr = slow
        while curr.next:
            next_val = curr.next
            curr.next = prev
            prev = curr
            curr = next_val

        curr.next = prev
        #check for max sum
        while curr:
            max_sum = max( max_sum , curr.val + head.val)
            head = head.next
            curr = curr.next
        return max_sum
