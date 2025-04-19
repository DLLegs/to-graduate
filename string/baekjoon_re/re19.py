# 백준 2581번 (약수, 소수 배수수)

M = int(input())
N = int(input())
MN_list = []

for i in range(M, N+1):
    if i < 2:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        MN_list.append(i)

if len(MN_list) == 0:
    print('-1')
else:    
    print(sum(MN_list))
    print(min(MN_list))