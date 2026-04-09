#실습 1번 구구단 출력
#1단~9단 출력, 한단마다 끊어지는 부분 만들기
# 2중 for문 이용

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print("-------------")
    