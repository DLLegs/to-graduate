# if문
# if문 등 while, for, def 등등 뒤에: 붙여줘야함
# if문 예시
money = 6000
if money >= 7000:
    print("택시")
else:
    print("걸어서")

# or, and, not 등 사용 가능
# in, not in 등 리스트 튜플 문자열로 사용가능

pocket = ['phone', 'card', 'key']
if 'card' in pocket:
    print("택시")

else:
    print("걸어서")

# pass 사용법
pocket = ['phone', 'card', 'key']
if 'card' in pocket:
    pass
else:
    print("돈이 없음")
# pocekt 리스트에 card가 존재하기 때문에 조건식은 출력하지 않음

# while문
treeHit = 0
while treeHit < 10:
 treeHit+=1
 print('%d번 찍음' %treeHit)
 if treeHit == 10:
     print("나무가 넘어갔습니다")


coffee = 10
coin = 20
while coin: # coin이 0이 아니기 때문에 항상 참
    print("돈을 지불했기에 커피를 줄게요")
    coffee = coffee -1
    print("남은 커피의 양은 %d개이다" %coffee)
    if coffee == 0:
        print("커피가 다 떯어졌습니다")
        break

# continue 활용해서 홀수만 출력 만들기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)

# while True 는 무한 루프 break나 ctrl + c 로 탈출 가능

# for문

Usually_for = [1, 2, 3]
for i in Usually_for:
    print(i) # 1, 2, 3 차례로 출력

marks = [90, 25, 35, 49, 88]

line = 0
for mark in marks:
    line = line + 1
    if mark > 65:
        print("%d번 학생은 합격입니다" %line)
    else:
        print("%d번 학생은 불합격입니다" %line)
# for문에도 continue 사용가능

# range 함수를 사용한 for
# range(시작숫자, 끝숫자)
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print(" ")