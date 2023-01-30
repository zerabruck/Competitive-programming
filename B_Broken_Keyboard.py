loop = int(input())

for i in range(loop):
    # print('hi')
    keys = list(input())
    pointer = 0
    # print(keys)

    while( pointer < len(keys) - 1):
        # print(len(keys))
        
        if keys[pointer] == keys[pointer + 1]:
            
            keys.pop(pointer)
            keys.pop(pointer)

        else:
            
            pointer += 1

    # keys.sort()
    sets = set(keys)
    ordered = sorted(sets) 
    strings = ''
    print(strings.join(ordered))
        