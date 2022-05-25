# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count=0
        next=head

        while(next.next!=None):
            count+=1
            next=next.next

        count+=1
        

        if (count%2!=0):
            count=count//2+1

        else:
            count=(count/2)+1

        next=head
        


        while(True):
            
            if(count==1):
                return next
            count-=1
            next=next.next
