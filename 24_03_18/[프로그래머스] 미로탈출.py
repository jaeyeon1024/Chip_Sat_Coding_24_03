from collections import deque


def solution(maps):

    row_len = len(maps)
    col_len = len(maps[0])

    visited = [[0 for _ in range(col_len)] for __ in range(row_len)] # 방문했는지 확인 밑 경로 길이 저장

    pos_row = 0
    pos_col = 0
    for i , rows in enumerate(maps): # 시작 지점 찾기
        for j , cols in enumerate(rows):
            if maps[i][j] == "L":
                pos_row = i
                pos_col = j
                break
        else:
            continue
        break

    discovered = deque([[pos_row,pos_col]])
    check = 0
    answer = 0

    def bfs(): # bfs 시작
        nonlocal discovered
        nonlocal visited
        nonlocal check
        nonlocal answer
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        while(True):
            if not discovered:
                break

            r,c = discovered.popleft()

            if maps[r][c] == "S" or maps[r][c] == "E": # 시작지점이거나 출구일 경우 체크하고 경로 길이 저장
                check += 1
                answer += visited[r][c]
            
            for i in range(4): # 각 위치 돌면서 저장
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < row_len and 0<= nc < col_len:
                    if maps[nr][nc] != "X" and visited[nr][nc] == 0: # 한번도 방문을 안했거나 벽이 아니라면
                        visited[nr][nc] = visited[r][c] + 1 # 다음 경로 저장
                        discovered.append([nr,nc])

    bfs()

    if check != 2: #끝났지만 출구랑 시작 지점 중 하나라도 못 갔으면 리턴 -1
        return -1
    
    return answer # 아니라면 정답 리턴
'''
    return -1 if check != 2 answer
'''


maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
ans = 16

print(solution(maps))

'''
시작하기 전: 

아마 bfs인거 같음 레버를 기준으로 bfs 하면서 앞으로 나가다가 start랑 exit 둘 다 찾으면 종료
혹은 더 이상 갈 수 있는 곳이 없는데 멈춰있으면 종료

시간 조금이라도 더 줄이는 방법
=> exit의 주변 혹은 exit에서 레버까지 bfs해서 찾기?
하지만 이거는 레버랑 exit랑 어디가 더 큰지 정해져 있지 않기 때문에 레버에서 부터 시작하는게 맞을 듯

'''