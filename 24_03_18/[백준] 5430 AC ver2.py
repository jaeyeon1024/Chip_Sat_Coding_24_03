import sys; input = sys.stdin.readline
from collections import Counter


case_num = int(input().strip())

for _ in range(case_num):
    orders = input().strip()

    order_count = Counter(orders)
    D_count = order_count["D"]
    R_count = order_count["R"]

    board_len = int(input().strip())

    board = []
    tmp = input().strip()[1:-1].split(',') # 양옆 괄호를 지우고 , 기준으로 split
    if tmp != ['']: board = list(map(int,tmp)) # 비어있는 공간이 아니라면 안에 있는 값에 int

    if D_count > board_len: # error 상황 제거
        print("error")
        continue

    start = 0
    end = board_len
    idx = 0
    
    for order in orders: # orders를 하나씩 꺼내오면서 앞에서 지우나 뒤에서 지우는거 선택
        if order == "R":
            idx = (idx+1) % 2
        if order == "D":
            if not idx:
                start+=1
                continue
            end -= 1

    if R_count % 2 == 0:# 최종적으로 reverse 되어있는지 안되어있는지 검사
        print('['+','.join(map(str,board[start:end]))+']')
    else:
        print('['+','.join(map(str,board[start:end][::-1]))+']')


'''
파이썬에서는 어려운 문제는 아닌거 같음
하지만 입력 받는거나 출력하는 거에서 틀려서 멘탈 나갈 뻔

틀린 이슈
[1234] R => [4,3,2,1]
마지막 print 할 때 그냥 list 출력이 아님

막 좋은 문제는 아닌듯    

인데 투포인터를 써서 풀 수도 있네 좋다

'''