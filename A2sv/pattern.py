loop = int(input())
string=input()
for i in range(1,loop):
    pattern=input()
    new_string=''
    for j in range(len(pattern)):
        if pattern[j] != string [j]:
            if pattern[j]=="?":
                new_string+=string[j]

            elif string[j] == "?":
                new_string+=string[j]

            else:
                new_string+="N"


        else:
            new_string+=pattern[j]

    string=new_string


result=''

for i in string:
    if(i=='N'):
        result+="?"

    elif i == '?':
        result+='n'

    else:
        result+=i

print(result)

    