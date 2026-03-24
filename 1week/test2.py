#실습2 간단한 사칙연산 계산기
'''
1. 두 개의 숫자 입력
2. 연산 수행
3. 결과 출력
'''

num1 = int(input("Number1 : "))
num2 = int(input("Number2 : "))

print(f"첫번쨰 숫자 : {num1}")
print(f"두번째 숫자 : {num2}")
print(f"더하기 : {num1+num2}")
print(f"빼기 : {num1-num2}")
print(f"곱하기 : {num1*num2}")
print(f"나누기 : {num1//num2}")