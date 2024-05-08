import sys
input = sys.stdin.readline

n = int(input().strip())

board = [list(map(int, input().split())) for _ in range(n)]

board = sorted(board, key=lambda x: (x[0], -x[1]))

answer = 0

start = board[0][0]
end = board[0][1]

for i in range(1, n):
    ns = board[i][0]
    ne = board[i][1]

    if ns <= end and ne > end:
        end = ne
        continue

    if ns > end:
        answer += end - start
        start = ns
        end = ne

answer += end - start
print(answer)
