# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_list = ''
        second_list = ''
        curr = l1
        while curr:
            first_list += str(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            second_list += str(curr.val)
            curr = curr.next

        second = int(second_list[::-1])
        first = int(first_list[::-1])
        result = first + second
        result = str(result)[::-1]
        dummy  = ListNode(0)
        curr = dummy
        for i in result:
            new = ListNode(int(i))
            curr.next = new
            curr = new
        return dummy.next
