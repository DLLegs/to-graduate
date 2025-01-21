# # 백준 10815

import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
cards = set(map(int, data[1:n+1]))
m = int(data[n+1])
had = list(map(int, data[n+2:]))

result = ['1' if card in cards else '0' for card in had]
print(' '.join(result))

# 백준 2751 (복습)

import sys
Input = sys.stdin.read
Data = Input().split()
List = list(map(int, Data[1:]))

List.sort()

print('\n'.join(map(str, List)))