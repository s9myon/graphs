n, m = list(map(int, input().split()))

matrix = []
for i in range(n):
    matrix.append(list())
    for j in range(n):
        matrix[i].append(0)

for _ in range(m):
    edge = list(map(int, input().split()))
    matrix[edge[0] - 1][edge[1] - 1] = 1
    matrix[edge[1] - 1][edge[0] - 1] = 1

for i in range(n):
    line = ""
    for j in range(n):
        if j != 0:
            line += f' {matrix[i][j]}'
        else:
            line += str(matrix[i][j])
    print(line)
