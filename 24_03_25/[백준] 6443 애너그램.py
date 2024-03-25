import sys; input = sys.stdin.readline
from typing import List
from itertools import permutations


cases = int(input().strip())

board = [input().strip() for _ in range(cases)]


for i in board:
    for j in sorted(set(permutations(i))):
        print("".join(j))