# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        try:
            prev = None
            front = None
            while head.next:
                front = head.next
                head.next = prev
                prev = head
                head = front 

            head.next = prev
            return head

        except:
            return


        
    
            
            
            
            
                
                
        