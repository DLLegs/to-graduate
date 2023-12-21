# 함수
# 기본 구조
# def 함수_이름(매개변수):
def add(a, b):
    return a + b
a = 3
b = 2
c = add(a, b) # add(3, 2)의 리턴값을 c에 대입
print(c) # 5 

# 매개변수(parameter)는 함수에 입력으로 전달된 값을 받는 변수
# 인수는 함수를 호출할 때 전달하는 입력값을 의미
# 위에서 보면 a, b는 매개변수 3, 4는 인수

def say():
    return 'Hi'

a = say()
print(a)  # Hi

# 리턴값이 없는 함수
def minu(a, b):
    print("%d, %d의 차 %d" %(a, b, a-b))
minu(6, 2)

#입력값도, 리턴값도 없는 함수
def iam():
    print("iam")
iam() # iam

# 매개변수를 직접 지정하여 호출
def mup(a, b):
    return a * b
result = mup(a = 2, b = 4) # a에 7, b에 3을 전달
print(result) # 8

# 여러 개의 입력값을 받는 함수 만들기
# def 함수_이름(*매개변수): * 주목
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result 
result = add_many(1, 2, 3)
print(result) # 6

def add_mul(choice, *args):
    if choice == "add": # 매개변수 choice에 "add"입력 받았을때
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul": # 매개변수 choice에 "mul"입력 받았을때
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5,6,7,8,9)
print(result) # 45
result = add_mul('mul',1, 2, 3)
print(result) # 6 

# lambda 예약어
# def와 동일한 기능, 보통 함수를 간결하게 한줄로 쓸때 사용
# 함수_이름 = lambda 매개변수1, 매개변수2, ...: 표현식
add = lambda a, b: a+b
result = add(3, 4)
print(result) # 7

