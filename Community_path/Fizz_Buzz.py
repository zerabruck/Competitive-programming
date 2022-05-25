class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        elements=[]
        for i in range(1,n+1):
            if(i%5==0 and i%3==0):
                elements.append("FizzBuzz")
            elif(i%3==0):
                elements.append("Fizz")
            elif(i%5==0):
                elements.append("Buzz")
            else:
                elements.append(f'{i}')
        return elements
        