n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

counter = 0
for i in range(len(matrix)):
    for elem in matrix[i]:
        if elem == 1:
            counter += 1

print(counter)
