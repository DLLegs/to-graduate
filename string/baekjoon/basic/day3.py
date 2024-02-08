# 딕셔너리
# 딕셔너리 이름 = {key1: value1, key2: value2, ...}

dic = {'name': 'kai', 'bnumber': '29'}
print(dic)

a = {'a': [1,2,3]} # value에 리스트도 넣을 수 있음

a['b'] = [1,2,3] # a 딕셔너리에 key b value [] 들어감
print(a)

print(a['a']) # a 딕셔너리 key a의 value 값을 가져옴

# key 값에 리스트[]는 사용불가 이지만 튜플()은 가능하다

# 집합 자료형 (set)
# 집합 자료형의 특징
# 중복을 허용하지 않는다, 순서가 없다

s1 = set([1,2,3])
print(s1) # {1, 2, 3}

s2 = set("hello")
print(s2) # {'h', 'o', 'e', 'l'}

#set 자료형에 저장된 값을 인덱싱으로 접근하려면
# 리스트나 튜플로 변환한 후 해야 한다.

t1 = tuple(s1)
print(t1) # 1, 2, 3
print(t1[0]) # 1