input()

summs = []

cards = list(map(int,input().split()))
total = sum(cards)

first = 0
second = len(cards) - 1

while(first <= second):
    if cards[first] >= cards[second]:
        summs.append(cards[first])
        first += 1

    else:
        summs.append(cards[second])
        second -= 1

sigma = sum([ summs[i] for i in range(0,len(summs),2)])
duressa = total - sigma

print(f'{sigma} {duressa}')