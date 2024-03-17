import sys; input = sys.stdin.readline
from collections import Counter
from collections import deque

case_num = int(input().strip())

for _ in range(case_num):
    orders = input().strip()

    order_count = Counter(orders)
    D_count = order_count["D"]
    R_count = order_count["R"]

    board_len = int(input().strip())
    board = []
    tmp = input().strip()[1:-1].split(',')
    if tmp != ['']: board = list(map(int,tmp))

    dq_board = deque(board)

    if D_count > board_len:
        print("error")
        continue
    
    idx = 0
    for order in orders:
        if order == "R":
            idx = (idx+1) % 2
        if order == "D":
            if not idx:
                dq_board.popleft()
                continue
            dq_board.pop()

    if R_count % 2 == 0:
        print('['+','.join(map(str,list(dq_board)))+']')
    else:
        print('['+','.join(map(str,list(dq_board)[::-1]))+']')


'''
파이썬에서는 어려운 문제는 아닌거 같음
하지만 입력 받는거나 출력하는 거에서 틀려서 멘탈 나갈 뻔
막 좋은 문제는 아닌듯    
'''