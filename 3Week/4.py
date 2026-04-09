for i in range(1, 10, 2):
    print(i)
for j in range(10, 1, -1):
    print(j)

for i in range(100):
    if i == 15:
        break
    elif i<10:
        print(i)
        continue
    print(f"10이상인 {i}이므로 펑")