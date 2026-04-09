#if문 활용 업다운 게임
import random
A = random.randint(1, 100)

while True:
    Q = int(input("숫자를 입력하세요(1~100): "))
    if Q == A:
        print("정답")
        break
    elif Q < A and Q >= 1:
        print("더 큰 수를 입력하세요.")
        print("정답을 모르시면 0을 입력하세요.")
    elif Q == 0:
        print("정답은 {}입니다.".format(A))
        break
    else:
        print("더 작은 수를 입력하세요.")
        print("정답을 모르시면 0을 입력하세요.")

