def distance(x, y):
    return (x**2 + y**2)**(1/2)


def solution(k, d):
    answer = 0

    pos_X = 0
    end = (d//k) * k
    pos_Y = end

    while (pos_X <= end):
        if distance(pos_X, pos_Y) > d:
            pos_Y -= k
            continue

        answer += (pos_Y//k) + 1

        pos_X += k
    return answer


k = 1
d = 5
print(solution(k, d))
