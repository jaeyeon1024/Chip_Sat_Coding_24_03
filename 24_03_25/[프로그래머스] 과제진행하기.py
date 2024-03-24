def solution(plans):
    stack = []
    answer = []
    board = sorted(plans,key= lambda x: x[1].split(":"))

    time_table_board = []
    for i in board:
        st_time = int(i[1].split(":")[0])*60 + int(i[1].split(":")[1])
        time_table_board.append([i[0],st_time,st_time+int(i[2]),int(i[2])])
    
    time_table_board.append([0,100000000,0])

    for i,val in enumerate(time_table_board[:-1]):
        if val[2] <= time_table_board[i+1][1]:
            answer.append(val[0])
            
            remain_time = time_table_board[i+1][1] - val[2]
            
            
            while(stack):
                pre = stack.pop()
                if remain_time >= pre[1]:
                    remain_time-=pre[1]
                    answer.append(pre[0])
                else:
                    pre[1] -= remain_time
                    remain_time = 0
                    stack.append(pre)
                    break
            
            continue

        stack.append([val[0],val[3]-time_table_board[i+1][1]+val[1]])
        
        #stack.append(val[0])
    return answer

plan  = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]

print(solution(plan))



'''
뭔가 시간 역순으로 해서 풀면 나올거 같은 느낌
시간은 그냥 다 분으로 변환해서 따로 저장 하면 될듯


'''