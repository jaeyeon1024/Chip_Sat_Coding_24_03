import sys; input = sys.stdin.readline
from typing import List
from collections import defaultdict


cases = int(input().strip())

board = [sorted(input().strip()) for _ in range(cases)]


answer = defaultdict(int)

def permutation(x:List ,y:List ,visited:List ,n:int,answer):
    
    if len(y) == n:
        answer["".join(y)] += 1
        if answer["".join(y)] == 1:
            print("".join(y))
        return answer
    
    
    for i in range(len(x)):
        if not visited[i]:
            y.append(x[i])
            visited[i] = True
            permutation(x,y,visited,n,answer)
            visited[i] = False
            y.pop()

for i in board:
    visited = [False]*len(i)

    permutation(i,[],visited,len(i),answer)