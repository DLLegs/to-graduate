# 백준 1427번 문제

N = list(map(int, str(input())))
N.sort(reverse=True)
for i in N:
    print(i, end='')