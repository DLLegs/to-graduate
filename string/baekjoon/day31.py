# 백준 9610번 문제

point_number = int(input())
Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0

for i in range(point_number):
    X, Y = map(int, input().split())
    
    if X > 0 and Y > 0:
        Q1 += 1
    elif X < 0 and Y > 0:
        Q2 += 1
    elif X < 0 and Y < 0:
        Q3 += 1
    elif X > 0 and Y < 0:
        Q4 += 1
    elif X == 0 or Y == 0:
        AXIS += 1
print("Q1:", Q1, "\nQ2:", Q2, "\nQ3:", Q3, "\nQ4:", Q4,"\nAXIS:", AXIS)

# 백준 8958번 문제

def cal_score(quiz_result):
    score = 0
    total = 0

    for answer in quiz_result:
        if answer == 'O':
            score += 1
            total += score
        else:
            score = 0
    return total

quiz_number = int(input())
for _ in range(quiz_number):
    quiz_result = input()
    result = cal_score(quiz_result)
    print(result)