# 백준 25206 (심화 1)

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0
result = 0
for _ in range(20):
    s,p,g = input().split()
    p = float(p)
    if g != 'P':
        total += p
        result += p * grade[rating.index(g)]

print('%.6f' % (result/total))

# 딕셔너리 사용 방식

grade_map ={
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, "C0": 2.0,
    'D+': 1.5, "D0": 1.0,
    'F': 0.0,
}

Total = 0.0
Result = 0.0

for _ in range(20):
    S,C,G = input().split()
    C = float(C)

    if G == 'P':
        continue

    Total += C
    Result += C * grade_map[G]

if Total == 0:
    print('0.000000')
else:
    print(f"{Result/Total:.6f}")