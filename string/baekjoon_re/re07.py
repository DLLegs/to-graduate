# 백준 10809 (문자열)

s = list(input())
alph = "abcdefghijklmnopqrstuvwxyz"

for a in alph:
    if a in s:
        print(s.index(a), end =" ")
    else:
        print(-1, end=" ")

