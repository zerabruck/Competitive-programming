# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_header=l1
        second_header=l2
        first_array=[]
        second_array=[]
        head1=l1
        head2=l2
        
        while(head1.next!=None):
            first_array.append(str(head1.val))
            head1=head1.next
            
        first_array.append(str(head1.val))
        
        while(head2.next!=None):
            second_array.append(str(head2.val))
            head2=head2.next
            
        second_array.append(str(head2.val))
        first_array.reverse()
        second_array.reverse()
        
        first_value=''
        second_value=''
        for i in first_array:
            first_value+=i
            
        for j in second_array:
            second_value+=j
            
        added_value=int(first_value) +int(second_value)
        added_value=str(added_value)
        added_value=added_value[::-1]
        new_header=first_header
        counter=0
        
        for i in added_value:
            counter+=1
            
            
            
            
            new_header.val=int(i)
            if(counter==len(added_value)):
                break
            if(new_header.next==None):
                
                new_header.next=second_header
            
            new_header=new_header.next
            
            
            
        if(new_header==None):
            return first_header
        else:
            new_header.next=None
            return first_header
            
        
        
                
            
        
        
        
        
        
        
            
    
        