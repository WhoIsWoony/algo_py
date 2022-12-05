"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""

### 환경세팅 ###
import sys                              
sys.stdin = open("./input.txt", "r")    #Tip1 : input.txt에 미리 입력을 복붙해놓으면 매번 복붙하는 것을 방지할 수 있다.
input = sys.stdin.readline              #Tip2 : 알고리즘용 빠른 읽기, 백준에서 유용
#sys.setrecursionlimit(10**6)           #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용

### 문제풀이용 ###
def solution(n, m, board):
    global answer
    answer = 0
    v = [[False]*m for _ in range(n)]

    def dfs(cr, cc, step, amount):
        global answer
        if step == 3:
            answer = max(answer, amount)
            return
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = cr + dr, cc + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if not v[nr][nc]:
                v[nr][nc] = True
                dfs(nr, nc, step+1, amount+board[nr][nc])
                v[nr][nc] = False
    
    def weird(cr, cc):
        global answer
        count = 0
        amount = board[cr][cc]
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = cr + dr, cc + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            count += 1
            amount += board[nr][nc]

        if count == 3:
            answer = max(answer, amount)
            return
        elif count == 4:
            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr, nc = cr + dr, cc + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= m:
                    continue
                answer = max(answer, amount - board[nr][nc])
                
    for r in range(n):
        for c in range(m):
            v[r][c] = True
            dfs(r, c, 0, board[r][c])
            v[r][c] = False
            weird(r, c)
    
    return answer
        
        
        
### 입력 ###
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, board))
