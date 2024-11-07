# 사용자가 입력한 숫자의 약수를 구하는 프로그램
number = int(input("Enter a number: "))  # 숫자를 입력받습니다.

# 1부터 입력받은 숫자까지의 약수를 찾기 위한 리스트 생성
divisors = [i for i in range(1, number + 1) if number % i == 0]

# 결과 출력
print("Divisors of", number, "are:", divisors)
