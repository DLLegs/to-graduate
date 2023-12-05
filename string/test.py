hour, min = map(int,input().split())
plus = int(input())

if min + plus >=60:
    Rmin = (min + plus) % 60
    hour = hour + ((min + plus) // 60)
else:
    min = min + plus
if hour >= 24:
    hour = hour - 24

print(hour, Rmin)