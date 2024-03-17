import sys; input = sys.stdin.readline


cases = []
for _ in range(1000):
    cs = int(input().strip())
    if not cs:
        break
    cases.append(cs)

board = [[0 for _ in range(31)] for __ in range(31)]

for i in range(31):
    for j in range(i+1):
        if i == 0:
            board[i][j] = 0
        elif j == 0:
            board[i][j] = 1
        else:
            board[i][j] = board[i-1][j] + board[i][j-1]

for i in cases:
    print(board[i][i])


'''
아니 이 문제를 가장 먼저 풀기 시작 했는데 가장 늦게 풀리는거 맞나 dp 개어렵네 내가 수학을 못하는 건가 진짜 다시 생각해봐야지 너는 꼭 푼다 진짜
드디어 찾았네 진짜 하 진짜 아니 H 하나 있는거랑 없는게 차이가 안나면 어쩌자는 거지 일단 굳


WH를 2차원으로 해놓고 default 는 0
여기서 W랑 H는 각각 W와 H개의 W랑 H를 가지고 있는 문자열의 수
[W][H] = [W-1][H] + [W-1][H-1] 인데 H는 W보다 클 순 없음 그럴 땐 0 으로 냅두고 continue
'''