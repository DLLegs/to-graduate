# 프로그램의 입출력
# 명령어 [인수1 인수2 ...]
#sys 모듈 사용하기

import sys

args = sys.argv[1:]
for i in args:
    print(i)