# 백준 1157번 문제
# 입력값: 알파벳 대소문자 문자열
# 출력값: 가장 많이 사용된 알파벳, 여러개면 ?

abc = input().upper()
abc_list = list(set(abc))
cabc = []

for i in abc_list:
    count = abc.count(i)
    cabc.append(count)

if cabc.count(max(cabc)) >=2 :
    print("?")
else:
    print(abc_list[(cabc.index(max(cabc)))])

# 백준 2941번 문제
# 입력값: 알파벳 소문자, '-', '='
# 출력값: 크로아티아 알파벳 표에 따른 크로아티아 알파벳

how_many = input()
modric_word = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in modric_word:
    how_many = how_many.replace(i,"x")
print(len(how_many))

# 백준 1316번 문제
# 입력값: 받을 단어 개수, 영어 소문자 단어
# 출력값: 그룹 단어의 개수

input_nWord = int(input())
gWnumber = input_nWord # 그룹 단어의 개수

for i in range(input_nWord):
    pgWord = input()
    for j in range(len(pgWord)-1):
        if pgWord[j] == pgWord[j+1]:
            continue
        elif pgWord[j] in pgWord[j+1:]: # 인덱스 j값이 해당 문자열에 더 존재하는 지
            gWnumber -=1
            break

print(gWnumber)

# 백준 25206번 문제
# 입력값: 20줄의 과목명, 학점, 등급 공백으로 구분
# 출력값: 전공평점

rate = 0 # 학점 * 과목평점
total = 0 # 학점의 총합
rating = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

for _ in range(20):
    subject, score, grade = input().split()
    if grade == "P":
        continue
    rate += float(score) * rating[grade]
    total += float(score)

print(rate/total)
