#예외 처리

#오류의 예시
"""
a = [1,2,3]
print(a[3])
"""
#try-except 문
#기본 구조
#try:
#except [발생오류 [as 오류변수]]:
try:
    4/0
except ZeroDivisionError as e:
    print(e) #오류변수 e에 담겨있는 오류 메시지 출력

#try-finally 문
#기본 구조
#try:
#finally:
#보통 finally 절은 사용한 리소스를 close해야 할 때 많이 사용
try:
    f = open('foo.txt', 'w')
    #무언가를 수행
    # (... 생략 ...)
finally:
    f.close() #중간에 오류가 발생해도 무조건 실행
    print("모든 파일이 닫혔습니다")

#여러 개의 오류 처리하기
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

#try문 에는 except 아래에 else절도 사용가능
#else: 오류가 없을 경우에만 실행

#오류 회피하기
try:
    f = open("없는 파일",'r')
except FileNotFoundError:
    pass

#예외 만들기
class MyError(Exception):
    def __str__(self):
        return "허용되지 않은 별명"
    
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)