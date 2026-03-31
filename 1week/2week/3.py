a = input("숫자 입력 : ")

if int(a) > 10:
    if int(a) <20:
        print(f"{a}는 10보다 크고 20보다 작다")
    else :
        print(f"{a}는 20보다 크다")
else :
    print(f"{a}는 10보다 작다")

b = int(input("숫자 입력 : "))
if b > 10 and b < 20:
        print(f"{b}는 10보다 크고 20보다 작다")
elif b > 20:
        print(f"{b}는 20보다 크다")
else :
        print(f"{b}는 10보다 작다")