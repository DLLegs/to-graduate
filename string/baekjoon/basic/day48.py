# 백준 2750번 문제

# 내장 함수
# N = int(input())
# numbers = [int(input() for _ in range(N))]

# numbers.sort()

# for num in numbers:
#     print(num)


# 버블 정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):  # n-1번의 패스 수행
        swapped = False  # 각 패스의 시작에서 swapped를 False로 초기화
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  # 인접한 두 요소를 비교
                arr[j], arr[j+1] = arr[j+1], arr[j]  # 교환
                swapped = True  # 교환이 발생하면 swapped를 True로 설정
        if not swapped:  # 만약 교환이 일어나지 않았다면 이미 정렬된 상태
            break


n = int(input())
numbers = [int(input()) for _ in range(n)]

bubble_sort(numbers)

for num in numbers:
    print(num)