# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head

        length = 1
        last = head
        while last.next:
            last = last.next
            length += 1
        

        k = k % length
        curr = head
        last.next = head
        for _ in range( length - k - 1 ):
            curr = curr.next

        

        head = curr.next
        curr.next = None
        return head
        
