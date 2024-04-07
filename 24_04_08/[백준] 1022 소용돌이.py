import sys
input = sys.stdin.readline


def find_num(r: int, c: int) -> int:

    tmp = 0

    cycle_num = max(abs(r), abs(c))
    cycle_size = cycle_num * 8
    cycle_start_row = cycle_num - 1 if cycle_num != 0 else 0
    cycle_start_col = cycle_num

    cycle_start_num = 4 * ((cycle_num**2) - cycle_num) + 2

    if r == 0\
            and c == 0:
        tmp = 1
    elif r == cycle_start_row \
            and c == cycle_start_col:
        tmp = cycle_start_num
    elif r > cycle_start_row:
        tmp = (cycle_start_num + cycle_size - 1) - (cycle_start_col-c)
    elif c == cycle_start_col:
        tmp = cycle_start_num + abs(r-cycle_start_row)
    elif r == cycle_start_row - (cycle_num * 2 - 1):
        tmp = cycle_start_num + (cycle_num * 2 - 1) + abs(c - cycle_start_col)
    else:
        tmp = cycle_start_num + (6 * (cycle_num-1) + 4) + r - cycle_start_row
    return tmp


r1, c1, r2, c2 = map(int, input().strip().split())

max_len = max(len(list(str(find_num(r1, c1)))),
              len(list(str(find_num(r2, c2)))))


board = []
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        tmp = find_num(i, j)
        for _ in range(max_len - len(str(tmp))):
            print(" ", end="")
        print(tmp, end=" ")
    print("")

'''

print(*map(lambda x: ' '*(max_len-len(x))+x, row))

와 맞네 이렇게 할걸 
'''