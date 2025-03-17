# 백준 2775번

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # 아파트 초기화
    apt = [[0] * (n+1) for _ in range(k+1)]

    # 0층 초기화(1호부터 n호까지)
    for i in range(1, n+1):
        apt[0][i] = i
    
    for floor in range(1, k+1):
        for room in range(1, n+1):
            apt[floor][room] = apt[floor][room-1] + apt[floor-1][room]
    
    print(apt[k][n])