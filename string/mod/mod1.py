#mod1.py
def add(a, b):
    return a + b
def sub(a, b):
    return a-b

# 직접 이 파일을 실행했을때 값이 참이 되어 if문 실행
# 대화형 인터프리터나 다른 파일에서 이 모듈 사용시
# 거짓이 되어 if문 실행 되지 않음
if __name__=="__main__":
    print(add(1, 4))
    print(sub(4, 2))
