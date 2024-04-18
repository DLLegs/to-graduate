# 백준 11399번 문제
# 그리디 알고리즘

N = int(input())
human = list(map(int, input().split()))

human.sort()
time = 0

for i in range(1, N + 1):
    time += sum(human[0:i])
print(time)

# 백준 1026번 문제
# 그리디 알고리즘

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
s = 0
for i in range(n):
    B_max = max(B)
    s += A[i] * B_max
    B.remove(B_max)
print(s)