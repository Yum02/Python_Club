a = [100, 500, 200, 400, 300]
max = 0
for i in a:
    if i > max:
        max = i
print(max) #리스트 a에서 가장 큰 값 반환하여 max에 저장하고 출력

b = [100, 500, 200, 400, 300]
print(max(b)) #리스트 b에서 가장 큰 값 반환하여 출력