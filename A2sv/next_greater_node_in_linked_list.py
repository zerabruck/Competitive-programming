# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ele = []
        curr = head
        while curr:
            ele.append(curr.val)
            curr = curr.next

        stack = [0]
        # print(ele)
        res = [0] * len(ele)
        for num in range(1 , len(ele)):
            if ele[stack[-1]] >= ele[num]:
                stack.append(num)
            else:
                while stack and ele[stack[-1]] < ele[num]:
                    var = stack.pop()
                    # print(ele[var])
                    res[var] = ele[num]

                stack.append(num)
        return res     
