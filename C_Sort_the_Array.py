loop = int(input())

numbers = list(map(int,input().split()))

sorte = sorted(numbers)

if sorte == numbers:
    print("yes")
    print(f'{1} {1}')

else:
    first = -1
    second = -1
    flag = False
    for i in range(len(numbers)-1,0,-1):
        # print(i)
        if flag :
            
            if numbers[i] > numbers[ i - 1] :
                second = i 
                break

            elif i - 1 == 0:
                second = 0
                break
        
        elif numbers[i] < numbers[i - 1]:
            if i-1 == 0:
                second = 0
            first = i
            flag = True



    if first == -1:
        # print('hi')
        print('no')

    else:
        revers = []
        # print(first)
        # print(second)
  
        for j in range(first,second - 1,-1):
            # print(numbers[j])
            # print(j)
            # print(numbers[j])

            revers.append(numbers[j])

        # print(revers)
        # print(revers)
        # print(revers)
        new_arr = numbers[:second] + revers + numbers[first + 1:]
        # print(new_arr)

        if new_arr == sorte:
            print("yes")
            print(f"{second + 1} {first + 1}")

        else:
            
            print("no")
 