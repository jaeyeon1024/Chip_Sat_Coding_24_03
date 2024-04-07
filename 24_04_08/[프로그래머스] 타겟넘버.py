from collections import defaultdict


def solution(numbers, target):
    answer = 0

    visit = defaultdict(list)

    # 큰거부터 처리하고 작은거 처리하는게 중복 발생해서 return 보내는 확률이 높지 않을까? 란 생각에
    numbers = sorted(numbers, reverse=True)

    def dfs(sums=0, cnt=0):
        nonlocal answer
        if len(numbers) == cnt:
            if sums == target:
                answer += 1
            return
        if sums in visit[cnt]:
            return

        dfs(sums+numbers[cnt], cnt+1)
        dfs(sums-numbers[cnt], cnt+1)

    dfs()

    return answer


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))  # "5"
