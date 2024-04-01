import sys
input = sys.stdin.readline


def main():
    n = int(input().strip())
    m = int(input().strip())
    strs = input().strip()

    ioi = "IOI"
    board = []

    answer = 0
    check = 0

    for i in range(m):
        if check:
            check = 0
            continue
        if strs[i:i+3] == "IOI":
            board.append(1)
            check = 1
            continue
        board.append(0)

    sums = 0
    sums_board = [0]

    for i in board:
        if i == 0:
            sums_board.append(0)
        else:
            sums_board[-1] += 1

    for i in sums_board:
        if i == 0:
            continue
        if i-n < 0:
            continue
        answer += i-n + 1

    print(answer)
    # print(sums_board)
    # print(board)
    return


main()

'''
OOIOIOIOIIOII

[0,0,1,1,1,0,1]



'''
