answer = 45
user = 0

while True:
    user = int(input("숫자 입력 : "))
    if user == answer:
        print("정답입니다.")
        break
    elif user < answer:
        print("더 큰 수를 입력하세요.")
    else:
        print("더 작은 수를 입력하세요.")
