import sys

input = sys.stdin.readline


n = int(input().strip())

dices = [list(map(int, input().split())) for _ in range(n)]

jump_idx_dic = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

answer = 0
# top bottom은 idx or value => idx
for i in range(6):
    bottom = i
    top = jump_idx_dic[bottom]
    print(dices)
    answer += max(
        dices[0],
        key=lambda x: (
            0 if dices[0].index(x) == top or dices[0].index(x) == bottom else x
        ),
    )
    print(answer)


"""

[1,0,0,0,0,1]   
[0,1,0,1,0,0]
[0,0,1,0,1,0]


시작

아래 선정 => 위 선정

제외한 가장 큰 숫자

다음층 가기
"""
