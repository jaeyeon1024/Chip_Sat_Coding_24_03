from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

n = int(input().strip())
graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def search(V):

    parent = [0] * (n+1)
    discoverd = [V]

    def dfs():
        nonlocal discoverd
        v = discoverd.pop()

        for i in graph[v]:
            if parent[i] != 0:
                continue
            parent[i] = v
            discoverd.append(i)
            dfs()

    dfs()
    return parent[2:]


for i in search(1):
    print(i)
