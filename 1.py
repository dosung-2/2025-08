# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n,m = map(int, input().split())
    num_list = list(map(int,input().split()))
    test_sum = sum(num_list[0:m])
    top_sum = test_sum
    min_sum = test_sum
    for i in range(m, n):
        test_sum= test_sum + num_list[i]
        test_sum= test_sum - num_list[i-m]
        if test_sum>top_sum:
            top_sum=test_sum
        if test_sum<min_sum:
            min_sum=test_sum
    print(f"#{test_case} {top_sum}")
    # ///////////////////////////////////////////////////////////////////////////////////\
    # 테스트 케이스 개수를 입력받아 정수로 변환
# T = int(input())  # 예: 3

for test_case in range(1, T + 1):
    # N: 전체 숫자의 개수, M: 연속해서 더할 숫자의 개수 입력받기
    N, M = map(int, input().split())  # 예: "10 5" → N=10, M=5
    # 숫자 리스트를 입력받아 정수형 리스트로 변환
    num_list = list(map(int, input().split()))  # 예: "1 2 3 4 5 6 7 8 9 10"

    # 첫 번째 윈도우(0번 인덱스부터 M-1번 인덱스까지)의 합을 구해서 초기값 설정
    window_sum = sum(num_list[0:M])
    max_sum = window_sum  # 현재까지 찾은 최대 연속합
    min_sum = window_sum  # 현재까지 찾은 최소 연속합

    # 리스트를 M부터 끝까지 순회하면서, 한 칸씩 윈도우를 이동
    for i in range(M, N):
        # 새로 진입한 값은 더하고, 윈도우를 벗어난 값은 뺀다
        window_sum += num_list[i]         # 윈도우 오른쪽에 새로 추가된 값
        window_sum -= num_list[i - M]     # 윈도우 왼쪽에서 빠진 값

        # 비교를 통해 최대/최소 값을 업데이트
        if window_sum > max_sum:
            max_sum = window_sum
        if window_sum < min_sum:
            min_sum = window_sum

    # #1, #2, … 형식으로 결과 출력: (최대 연속합 – 최소 연속합)
    print(f"#{test_case} {max_sum - min_sum}")
