import sys; input = sys.stdin.readline


cases = []
for _ in range(1000):
    cs = int(input().strip())
    if not cs:
        break
    cases.append(cs)

print(cases)