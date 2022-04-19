#  answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#  answer[i] == "Fizz" if i is divisible by 3.
#  answer[i] == "Buzz" if i is divisible by 5.
#  answer[i] == i (as a string) if none of the above conditions are true.

n=15
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


print(elements)

