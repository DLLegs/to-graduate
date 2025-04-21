# 백준 11653번 (약수, 배수, 소수)

N = int(input())
tmp = N

while(1):
    if N == 1:
        break
    else:
        for i in range(2, N+1):
            if N % i == 0:
                print(i)
                N = N // i
                break