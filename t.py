n, m = list(map(int, input().split()))

matrix = []
for i in range(n):
    matrix.append(list())
    for j in range(n):
        matrix[i].append(0)

edges = []
for _ in range(m):
    edge = list(map(int, input().split()))
    matrix[edge[0] - 1][edge[1] - 1] += 1
    matrix[edge[1] - 1][edge[0] - 1] += 1

flag = True
for i in range(n):
    for j in range(n):
        if i != j:
            if matrix[i][j] != 1:
                flag = False
                break
    if not flag:
        break
if flag:
    print("Yes")
else:
    print("No")
