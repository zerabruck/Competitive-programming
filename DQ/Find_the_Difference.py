s = "abcde "
t = "abcdef"
list_of_t=[]


sotre=''
for i in t:
    list_of_t.append(i)
    print(list_of_t)

for i in s:
    if(i in list_of_t):
        list_of_t.remove(i)

for i in list_of_t:
    sotre+=i
        
print(sotre)

