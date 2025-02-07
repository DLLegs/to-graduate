# # 백준 1929번 문제

# m, n = map(int, input().split())
# prime_list = []

# def prime_check(x):
#     if x < 2:
#         return False
#     if x == 2 or x == 3:
#         return True
#     if x % 2 == 0 or x % 3 == 0:
#         return False
    
#     i = 5
#     while i*i <= x:
#         if x % i == 0 or x % (i+2) == 0:
#             return False
#         i += 6
#     return True

# for i in range(m, n+1):
#     if prime_check(i):
#         prime_list.append(i)

# print('\n'.join(map(str, prime_list)))

# 백준 4134번 복습

import sys
input = sys.stdin.read
data = list(map(int, input().split()))
n = data[0]
test_case = data[1:]

def is_prim(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x%2==0 or x%3==0:
        return False
    
    i = 5
    while i*i <= x:
        if x%i==0 or x%(i+2)==0:
            return False
        i += 6
    return True

for i in test_case:
    while not is_prim(i):
        i += 1
    print(i)