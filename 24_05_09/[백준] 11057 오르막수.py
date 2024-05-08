import sys
input = sys.stdin.readline

n = int(input().strip())

board = [[1] + [0]*9 for _ in range(n+1)]

for i in range(n+1):
    for j in range(10):
        board[i][j] = board[i-1][j] + board[i][j-1]

print(sum(board[n-1]) % 10007)
