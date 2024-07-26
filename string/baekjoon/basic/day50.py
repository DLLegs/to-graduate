# 백준 2501번 문제

N, K = map(int,input().split())


def divisor(N) :
    divisorList = []
    for i in range(1, N+1):
        if (N % i == 0):
            divisorList.append(i)
    return divisorList

divisor_list = divisor(N)

if K <= len(divisor_list):
    print(divisor_list[K-1])
else:
    print(0)