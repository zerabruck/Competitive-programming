class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next



class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.length = 0     

    def get(self, index: int) -> int:
        if self.length <= index  :
            return -1

        curr = self.dummy.next
        for i in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.dummy.next
        self.dummy.next = new
        self.length += 1
     

    def addAtTail(self, val: int) -> None:
        curr =self.dummy
        while curr.next:
            curr = curr.next

        new = Node(val)
        curr.next = new
        self.length += 1
 
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
        curr = self.dummy
        for i in range(index):
            curr = curr.next

        new = Node(val)
        new.next = curr.next
        curr.next = new 
        self.length += 1
   

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return 

        curr = self.dummy
        for i in range(index):
            curr = curr.next

        curr.next = curr.next.next
        self.length -= 1

        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
