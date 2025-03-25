# 백준 4948

import sys

Max = 246912
is_prime = [True] * (Max + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(Max**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, Max + 1, i):
            is_prime[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    count = sum(1 for i in range(n+1, 2*n+1) if is_prime[i])
    print(count)