# 백준 15552
import sys

T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

# 백준 10951번

import sys

while(True):
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)
    except:
        break