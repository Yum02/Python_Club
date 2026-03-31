score = int(input("점수 입력 : "))

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score < 90:
    print("B")
elif score >= 70 and score < 80:
    print("C")
elif score >= 60 and score < 70:
    print("D")
elif score < 60 and score >= 0:
    print("F")
else :
    print("Error : 0~100 사이의 숫자를 입력해주세요.")