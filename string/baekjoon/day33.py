# 백준 11557번 문제

T = int(input())

for i in range(T):
    N = int(input())
    university_name = ""
    max_drinks = 0
    for i in range(N):
        x, y = input().split()
        y = int(y)
        if y > max_drinks:
            university_name = x
            max_drinks = y
    print(university_name)

# 백준 10757번 문제

A, B = map(int, input().split())
result = A + B
print(result)