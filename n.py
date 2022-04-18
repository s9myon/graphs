n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

s = []
for j in range(n):
    s.append(0)
    for i in range(n):
        s[j] += matrix[i][j]

c = []
for i in range(n):
    c.append(0)
    for j in range(n):
        c[i] += matrix[i][j]

for i in range(n):
    print(f'{s[i]} {c[i]}')
