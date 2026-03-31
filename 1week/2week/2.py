#조건문
a = 10
b = 20
if a>b:
    print(f"{a}는 {b}보다 크다")
else :
    print(f"{a}는 {b}보다 작다")

sysstat = input("system status(ok or anything) :")
if sysstat == "ok":
    print("시스템이 정상입니다.")
else :
    print("시스템에 문제가 있습니다.")

x = input("숫자 입력(0~100) : ")
if int(x) >= 90:
    print("A")
elif int(x) >= 80:
    print("B")
elif int(x) >= 70:
    print("C")
elif int(x) >= 60:
    print("D")
elif int(x) <60 and int(x) >= 0:
    print("F")
else :
    print("Error : 0~100 사이의 숫자를 입력해주세요.")