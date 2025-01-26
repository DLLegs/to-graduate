# 백준 10816번 문제 (복습)

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
cards = list(map(int, data[1:n+1]))
m = int(data[n+1])
had = list(map(int, data[n+2:]))

card_count = {}
for num in had:
    card_count[num] = card_count.get(num,0)+1

result = [str(card_count.get(card,0)) for card in cards]

print(' '.join(result))