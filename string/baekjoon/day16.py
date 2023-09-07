# 백준 10818번 문제
# 입력값: 정수의 개수, 정수의 리스트
# 출력값: 리스트의 최솟값 최대값

num = int(input())
nList = list(map(int, input().split()))
print(min(nList), max(nList))

# 백준 2562번 문제
# 입력값: 9개의 자연수
# 출력값: 최대값과 몇 번째 숫자인지

maxWhat = []
for i in range(9):
    maxWhat.append(int(input()))
print(max(maxWhat))
print(maxWhat.index(max(maxWhat))+1)

# 백준 10813번 문제
# 입력값: 총 바구니의 개수, 교환 횟수, 교환 바구니
# 출력값: 바구니에 있는 공의 숫자

N, M = map(int,input().split())
basket = [i for i in range(1,N+1)] # 리스트 컨프리헨션

for i in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
for i in range(N):
    print(basket[i], end = ' ')

# 백준 5597번 문제
# 입력값: 총 28줄(출석번호)
# 출력값: 30까지중 없는 번호

student = [i for i in range(1,31)]

for _ in range(28):
    num = int(input())
    student.remove(num)

print(min(student))
print(max(student))

# 백준 3052번 문제
# 입력값: 총 10개의 정수
# 출력값: 42로 나눴을때 나머지가 다른 개수

devList = []
for i in range(10):
    a = int(input())
    devList.append(a%42)
print(len(set(devList)))    

# 백준 10811번 문제
# 입력값: 바구니의 갯수, 바꿀 횟수, 범위
# 출력값: 바구니의 순서

N, M = map(int, input().split())
box = [i for i in range(1, N+1)]

for i in range(M):
    i, j = map(int, input().split())
    temp = box[i-1:j]
    temp.reverse()
    box[i-1:j] = temp

for i in range(N):
    print(box[i], end=' ')

# 백준 1546번 문제
# 입력값: 과목 개수, 현재 성적
# 출력값: 새로운 과목 평균

num = int(input())
gList = list(map(int, input().split()))
M = max(gList)

for i in range(num):
    gList[i] = gList[i]/M * 100
print(sum(gList)/num)