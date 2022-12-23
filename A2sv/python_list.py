if __name__ == '__main__':
    N = int(input())
    list_elements=[]
    
    for i in range(N):
        commands=input().split()
        if(commands[0]=='insert'):
            list_elements.insert(int(commands[1]),int(commands[2]))
            
        elif(commands[0]=='print'):
            print(list_elements)
            
        elif(commands[0]=='remove'):
            list_elements.remove(int(commands[1]))
            
        elif(commands[0]=='append'):
            list_elements.append(int(commands[1]))
            
        elif(commands[0]=='sort'):
            list_elements.sort()
            
        elif(commands[0]=='pop'):
            list_elements.pop()
            
        elif(commands[0]=='reverse'):
            list_elements.reverse()
            