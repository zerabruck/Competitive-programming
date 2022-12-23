if __name__ == '__main__':
    loop=int(input())
    
    input_list=list(map(int,input().split()))

    t=tuple(input_list)
    hased_value=hash(t)
    print(hased_value)
