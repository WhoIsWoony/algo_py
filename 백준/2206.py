import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline


"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
### 문제풀이용 ###
from collections import deque
def solution(n, m, board):
    vw = [[[0, 0] for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0,0,1))
    vw[0][0][1] = 1
    
    while q:
        cr, cc, chance = q.popleft()

        if cr == n-1 and cc == m-1:
            return vw[cr][cc][chance]

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr and nr < n and 0 <= nc and nc < m: #check boundary
                if board[nr][nc] == 0 and vw[nr][nc][chance] == 0: #no wall
                    q.append((nr, nc, chance))
                    vw[nr][nc][chance] = vw[cr][cc][chance] + 1
                elif board[nr][nc] == 1 and chance == 1: #if wall
                    q.append((nr, nc, chance-1))
                    vw[nr][nc][0] = vw[cr][cc][chance] + 1
                
    return -1

### 입력 ###
n, m = map(int, input().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
print(solution(n, m, board))                        #풀이용
