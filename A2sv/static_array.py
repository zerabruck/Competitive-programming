class StaticArrays:
    def __int__(self,arr = [0,0,0,0] , capacity = 4,length = 0):
        self.arr=arr
        self.capacity = capacity
        self.length = length

    def insertEnd(self,value):
        if self.length == self.capacity:
            return None
        else:
            self.arr[self.length] = value
            self.length += 1

    def removeEnd (self):
        if self.length == 0:
            return None
        else:
            self.arr[self.length] = 0
            self.length -= 1

    def insertMiddle(self,index,value):
        if self.length == self.capacity:
            return None
        else:
            inserted = value 
            for i in range(index,self.length + 1):
                inserted,self.arr[i] = self.arr[i] , inserted
        