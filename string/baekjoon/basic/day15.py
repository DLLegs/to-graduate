# 백준 25304번 문제
# 입력값: 첫째 줄(총 금액), 둘째 줄(종류 수), 이후(금액과 수량)
# 출력값: 일치하면(yes), 다르면(no)

Total= int(input())
sumNum = int(input())
sum = 0

for i in range(sumNum):
    ePrice, eNum = map(int, input().split())
    sum = sum + ePrice * eNum

if sum == Total:
    print("Yes")
else:
    print("No")

# 백준 25314번 문제
# 입력값: N바이트 정수
# 출력값: N // 4 int 형태

Nbyte = int(input())

fin = "int"
for i in range(Nbyte//4):
    fin = 'long ' + fin
print(fin)

# 백준 15552번 문제
# 입력값: 줄 개수, 더할 값 2개
# 출력값: 줄 개수에 따른 두 값의 합
import sys

num = int(sys.stdin.readline())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


# 백준 10807번 문제
# 입력값: 정수의 개수,  정수 열, 찾을 정수의 위치
# 출력값: 위치해 있는 정수

num = int(input())
nList = list(map(int, input().split()))
loc = int(input())

print(nList.count(loc))