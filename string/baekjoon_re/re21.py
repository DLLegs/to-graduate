# 백준 1085번 (직사각형)

x, y, w, h = map(int, input().split())

print(min(x,y,w-x,h-y))