class DataStream:
    """
    what i am thinking here is that if we create a list of size k and then when a new element
    enters the stream i will have a circular pointer that point will point where to put the
    stream in. while i eneter the elements i will check if there are different elements than
    the value and if there is i will increase the value of difference and when i replace the
    elements i wll check if the replaced element is similar to the value and if it is not 
    i will decrease the value of similarity and then check the new element that will eneter
    stream and i will add or not the difference value based on the value 
    """

    def __init__(self, value: int, k: int):
        self.value = value
        self.cut = k
        self.data_stream =[]
        self.pointer = 0
        self.difference = 0

        
    def consec(self, num: int) -> bool:
        if len(self.data_stream) < self.cut:
            if num != self.value:
                self.difference += 1
            self.data_stream.append(num)
            if self.difference == 0 and len(self.data_stream) == self.cut:
                return True
            return False
        if self.pointer == self.cut:
            self.pointer = 0

        if self.data_stream[self.pointer] != self.value:
            self.difference -= 1

        self.data_stream[self.pointer] = num
        self.pointer += 1
        if num != self.value:
            self.difference += 1

        if self.difference == 0:
            return True
        return False


        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)