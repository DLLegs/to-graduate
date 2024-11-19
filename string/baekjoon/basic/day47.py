# # 백준 1436번 문제

n = int(input())
nth = 666
count = 0

while True:
    if '666' in str(nth):   #1 n번째 수에 '666'이 포함되어 있다면(str이 아니면 무조건 1의자리부터 시작하니까)
        count+=1               #2 카운트를 올려라
    if count == n:          #4 카운트랑 n번째 수가 같다면 
        print(nth)           #5 nth를 출력하고
        break               #6 while문을 종료해라
    nth+=1 

## 백준 1193번 문제

# # 규칙
# # 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2
# # 1 -> 2 -> 3 -> 4 -> 5

N = int(input())
line = 1

while N > line:  # 대각선 라인을 찾기위해서
    N -= line
    line += 1

if line % 2 == 0:
    up = N
    down = line - N + 1