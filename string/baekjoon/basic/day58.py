# 백준 5073번 문제
# equilateral: 세 변의길이가 모두 같은 경우
# isosceles: 두 변의 길이만 같은 경우
# scalene: 세 변의 길이가 모두 다른 경우
# invalid: 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    elif sum((a,b,c)) - max((a,b,c)) <= max((a,b,c)):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")