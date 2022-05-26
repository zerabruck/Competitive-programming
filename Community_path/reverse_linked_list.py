# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return head
        elif(head.next==None):
            return head
        elif(head.next.next==None):
            value=head.next
            head.next=None
            value.next=head
            return value
        else:
            value=head
            first=value
            second=value.next
            head.next=None
            while(second.next.next!=None):
                third=second.next
                second.next=first
                first=second
                second=third
            third=second.next
            second.next=first
            third.next=second
            return third
    
            
            
            
            
                
                
        