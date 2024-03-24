import sys; input = sys.stdin.readline
import re
from collections import Counter
from itertools import combinations

def distance(x,y):
    return sum(map(int,(bin(x^y)[2:])))

def vec_sum(x,y,z):
    
    return distance(x,y)+distance(x,z)+distance(y,z)

cases = int(input().strip())

for __ in range(cases):
    num = int(input().strip())

    board = input().strip()
    board = re.sub("[ENTP]","1",board)
    board = re.sub("[ISFJ]","0",board).split(" ")
    
    board = list(map(lambda x: int(x,2),board))
    dic_board = Counter(board)

    if dic_board.most_common(1)[0][1] >= 3:
        print(0)
        continue
    if num >= 33:
        print(0)
        continue
    elif num >= 17:
        print(2)
        continue

    print(min(map(lambda x: vec_sum(x[0],x[1],x[2]),combinations(board,3))))