import sys

# 명령줄 인수 확인
if len(sys.argv) < 2:
    print("Usage: python divisors.py <number>")
    sys.exit(1)  # 프로그램 종료

# 명령줄에서 숫자 입력받기
number = int(sys.argv[1])

# 1부터 number까지 반복하며 약수를 찾기
for i in range(1, number + 1):
    if number % i == 0:  # 나머지가 0이면 약수
        print(i, end=" ")

# 마지막 줄바꿈
print()
