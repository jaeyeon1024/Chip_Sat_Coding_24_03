import sys; input = sys.stdin.readline




cases = int(input().strip())

board = [sorted(input().strip()) for _ in range(cases)]

def permutation(arr:list,n:int):

    visited = [False] * n

    def generate(li:list,visited:list,check:list):

        if len(li) == n:
            print("".join(li))
            return
        
        for i in range(n):
            if visited[i] or arr[i] in check:
                continue
            
            li.append(arr[i])
            visited[i] = True
            generate(li,visited,[])
        
            check.append(li[-1])
            
            visited[i] = False
            li.pop()
            
        return

    generate([],visited,[])

    return

for case in board:
    permutation(case,len(case))
