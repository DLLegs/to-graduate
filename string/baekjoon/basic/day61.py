# 백준 2231번 문제

# 예를 들어, 245의 분해합은 256(=245+2+4+5)

N = int(input())

for i in range(N):
    M = i + sum(map(int, str(i)))
    if N == M:
        print(i)
        break
else:
    print(0)