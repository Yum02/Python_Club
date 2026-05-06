#리스트
number1 = 123
number2 = 456
number3 = 789

number_list = [number1, number2, number3]
print(number_list)

x = [0, 1, 3, 4]
x.append(5)
print(x) #x 리스트에 데이터 5 추가

x.remove(3)
print(x) #x 리스트에서 데이터 3 제거

y = [2, 6, 13, 1]
y.sort()
print(y) #y 리스트를 오름차순으로 정렬
y.sort(reverse=True)
print(y) #y 리스트를 내림차순으로 정렬

z = [1, 2, 3, 4, 5]
z.insert(0, 0)
print(z) #z 리스트의 인덱스 0 위치에 데이터 0 추가

z.pop(4)
print(z) #z 리스트에서 인덱스 4 위치의 데이터 제거

print(len(z)) #z 리스트의 길이 반환