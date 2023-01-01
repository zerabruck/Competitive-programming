loop = int(input())

for i in range(loop):
    course= input().split()
    dicto={}

    for word in course:
        string=''
        inter=''
        for char in word:
            if(48<=ord(char)<=57):
                inter+=char
            else:
                string+=char

        dicto[int(inter)]=string


    sorted_dicto=sorted(dicto)

    sorte=' '.join([ dicto[i] for i in sorted_dicto])
    print(sorte)

            
# dicto={3:"lakjdsf",2:";alksdjf"}
# new=sorted(dicto)
# print(new)
