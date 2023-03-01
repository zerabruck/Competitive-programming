# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merger(self , dummy , list1 , list2 ):
        if  not list1:
            dummy.next = list2
            return
        elif not list2:
            dummy.next = list1
            return

        if list1.val <= list2.val :
            dummy.next = list1
            self.merger(list1 , list1.next , list2)
            return 

        else:
            dummy.next = list2 
            self.merger(list2 ,list1 , list2.next)
            return


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        self.merger(dummy , list1 , list2)
        return dummy.next
