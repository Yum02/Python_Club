a = [100, 200, 200, 300, 400, 500]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

x = [100, 200, 200, 300, 400, 500]
y = list(set(x))
y.sort(reverse=True)
print(y)
