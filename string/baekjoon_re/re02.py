# 2884번 알람 시계

h, m = map(int, input().split())

def clock(h, m):
    
    if m < 45:
        m = m - 45 + 60
        h -= 1
    else:
        m -= 45

    if h > 23:
        h = 0
    elif h < 0:
        h = 23
    
    print(h, m)

clock(h, m)