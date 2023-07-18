# 클래스 class

# 클래스의 예시
# calculator3
class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator() # cal1은 객체라 부름
cal2 = Calculator() # cal2은 객체라 부름

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

"""객체와 인스턴스의 차이
클래스로 만든 객체를 ‘인스턴스’라고도 한다. 
그렇다면 객체와 인스턴스의 차이는 무엇일까? 
이렇게 생각해 보자. a = Cookie()로 만든 a는 객체이다. 
그리고 a 객체는 Cookie의 인스턴스이다. 
즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용한다.
‘a는 인스턴스’보다 ‘a는 객체’라는 표현이 어울리며 
‘a는 Cookie의 객체’보다 ‘a는 Cookie의 인스턴스’라는 표현이 훨씬 잘 어울린다.
"""

class FourCal:
    
    def setdata(self, first, second): # 메서드
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.first)
print(b.second)

print(a.add())
print(b.add())

print(a.mul())
print(b.mul())

print(a.sub())
print(b.sub())

print(a.div())
print(b.div())


# 생성자
