# 패키지
# 패키지란 관련 있는 모듈의 집합
# 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해줌

# echo 모듈을 import 하는 3가지 방법

import package.sound.echo
package.sound.echo.echo_test()

from package.sound import echo
echo.echo_test()

from package.sound.echo import echo_test
echo_test()

# __init__.py의 용도
# 위 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할
# 위 파일은 패키지와 관련된 설정이나 초기화 코드를 포함
# 패키지 수준에서 변수와 함수를 정의 가능
# 패키지의 __init__.py 파일에 공통 변수나 함수를 정의 가능

import package
print(package.VERSION)


import package.graphic.render
package.graphic.render.render_test()