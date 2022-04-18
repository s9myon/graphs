n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

answer = ""
for i in range(len(matrix)):
    counter = 0
    for elem in matrix[i]:
        if elem == 1:
            counter += 1
    if i != 0:
        answer += " " + str(counter)
    else:
        answer += str(counter)
print(answer)
