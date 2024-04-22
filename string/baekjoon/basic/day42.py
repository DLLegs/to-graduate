# 백준 9063번 문제

N = int(input())
X_list = []
Y_list = []

for _ in range(N):
    x, y = map(int, input().split())
    X_list.append(x)
    Y_list.append(y)

print((max(X_list) - min(X_list)) * (max(Y_list) - min(Y_list)))