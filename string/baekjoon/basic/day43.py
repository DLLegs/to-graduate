# 백준 10101번 문제

A = int(input())
B = int(input())
C = int(input())
total = A + B + C

if A == B == C == 60:
    print("Equilateral")
elif total == 180 and (A == B or A == C or B == C):
    print("Isosceles")
elif total == 180 and A != B != C:
    print("Scalene")
else:
    print("Error")