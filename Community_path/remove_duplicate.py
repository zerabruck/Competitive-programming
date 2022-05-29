# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first=head
        prev=head
        if(prev==None):
            return prev
        head=head.next
        if(head==None):
            return prev
        
        
        while(head.next!=None):
            
            
            if(head.val==prev.val):
                prev.next=head.next
                temp=head.next
                head.next=None
                
                head=temp
                if(temp==None):
                    break
                continue 
            prev=head
            head=head.next
        
                
        try:
            if(head.val==prev.val):
                
                prev.next=None
            return first
                
        except:
            return first 
            
        