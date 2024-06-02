def solution(n, left, right):
    answer = []

    for i in range(left, right+1):

        answer.append(max((i % n) + 1, (i // n)+1))

    return answer


n = 4
left = 7
right = 14

print(solution(n, left, right))

'''

1 2 3 4 5
2 2 3 4 5
3 3 3 4 5
4 4 4 4 5 
5 5 5 5 5


범위를 나누는거 부터이지 않을까?
범위를 나누고 하는거? 보다 쭉 돌면서 범위 찾는거
어 그게아니라 그냥 각 순서랑 현재 인덱스 max해서 찾으면 되는건가

'''
