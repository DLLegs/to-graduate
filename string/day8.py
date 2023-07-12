# 파일 입출력
# 파일_객체 = open(파일_이름, 파일_열기_모드)
# 열기_모드 r, w, a

f = open("새파일.txt", 'w')
f.close()

f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'w')
f.close()

# 위 예시는 파일을 쓰기 모드로 열기만 했고 아무것도 쓰지 않음

f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'w')
for i in range(1, 11):
    data = "%d 번째 줄이다 \n" %i
    print(data)
    f.write(data)
f.close()

# 파일을 읽는 방법들

# readlie 함수 이용
f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'r')
line = f.readline()
print(line)
f.close()
# 위 프로그램은 파일의 가장 첫번째 줄만 출력

#모든 줄 출력
f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'r')
while True:
    line = f.readline()
    if not line: break # 더 이상 읽을 줄이 없으면 break
    print(line)
f.close()

# readlines 함수 이용
# 모든 줄을 읽어옴
f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'r')
lines = f. readlines()
for line in lines:
    print(line)
f.close()

# read 함수 사용
# 문자열로 리턴하기에 /n 생략
f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'r')
data = f.read()
print(data)
f.close()

# 파일 객체(f)는 for 문과 함께 사용하여 파일을 줄 단위로 읽어옴
f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'r')
for line in f:
    print(line)
f.close()

#파일에 새로운 내용 추가하기
f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'a')
for i in range(11, 20):
    data = "%d 번째 줄이다\n" %i
    f.write(data)
f.close()

f = open("C:/Users/xoals/OneDrive/문서/test.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()