n = int(input("숫자를 입력하세요: "))

#별 쌓기
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()

m = int(input("숫자를 입력하세요: "))

for i in range(m):
    for j in range(m-i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    print()