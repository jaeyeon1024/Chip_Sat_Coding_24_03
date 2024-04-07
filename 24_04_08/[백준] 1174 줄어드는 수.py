import sys
input = sys.stdin.readline


num = int(input().strip())

board = [[0] * 11 for _ in range(10)]

for i in range(10):
    for j in range(10):
        if i == 0:
            board[i][j] = 1
            continue
        if j == 0:
            board[i][j] = 0
            continue
        board[i][j] = board[i-1][j-1] + board[i][j-1]
    board[i][10] = sum(board[i])

# print(board)

tmp = 0

for i, bd in enumerate(board):
    if bd[-1] >= num:
        tmp = i
        break
    num -= bd[-1]
else:
    print(-1)
    exit(0)  # 여기서 종료 해야함

ans = []

for i in range(tmp, -1, -1):
    for j, val in enumerate(board[i]):
        if not val:
            continue
        if num - val <= 0:
            ans.append(str(j))
            break
        num -= val


print("".join(ans))

'''

[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10], 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 45], 
[0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 120], 
[0, 0, 0, 1, 4, 10, 20, 35, 56, 84, 210], 
[0, 0, 0, 0, 1, 5, 15, 35, 70, 126, 252], 
[0, 0, 0, 0, 0, 1, 6, 21, 56, 126, 210], 
[0, 0, 0, 0, 0, 0, 1, 7, 28, 84, 120], 
[0, 0, 0, 0, 0, 0, 0, 1, 8, 36, 45], 
[0, 0, 0, 0, 0, 0, 0, 0, 1, 9, 10], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]


'''
