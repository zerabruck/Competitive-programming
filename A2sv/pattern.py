loop = int(input())
result=[]
for i in range(loop):
    string = input()
    if len(result) == 0:
        [ result.append(i) for i in string]


    else:
        for j in range(len(string)):
            if result[j] != string[j]:
                if result[j] == "?":
                    result[j]=string[j]

                elif string[j] != "?":
                    result[j] = False

                

answer = ''

for i in result:
    if i == "?":
        answer += "g"
    elif i == False:
        answer += "?"

    else:
        answer += i

print(answer)
                    
