# 백준 10871번

N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []

for i in A:
    if i < X:
        print(i, end=" ")

# 백준 10818번

n = int(input())
a = list(map(int, input().split()))

a.sort()
print(a[0],a[-1])