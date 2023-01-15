input()
arr = list(map(int,input().split()))

neg_set = []
pos_set = []
zero_set = []


for i in arr:
    if i < 0:
        neg_set.append(str(i))
    elif i == 0:
        zero_set.append(str(i))

    else:
        pos_set.append(str(i))

if len(pos_set) == 0:
    pos_set.append(neg_set.pop())
    pos_set.append(neg_set.pop())

if len(neg_set) % 2 ==0:
    zero_set.append(neg_set.pop())

string_pos =  f'{len(pos_set)} ' +  ' '.join(pos_set)
string_zero = f'{len(zero_set)} ' + ' '.join(zero_set)
string_neg = f'{len(neg_set)} ' + ' '.join(neg_set)

print(string_neg)
print(string_pos)
print(string_zero)

