loop = int(input())

for i in range(loop):
    input()
    input_array = list(map(int,input().split()))
    input_string = input()
    dicto = {}


    if len(input_array) != len(input_string):
        print("NO")
        continue

    for index,value in enumerate(input_array):
        if value not in dicto:
            dicto[value] = input_string[index]

    check_string = "".join([dicto[i] for i in input_array])
    

    if check_string == input_string:
        print("YES")
    else:
        print("NO")



