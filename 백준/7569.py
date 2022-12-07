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
sys.setrecursionlimit(10**6)           #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용
INF = int(1e9)

### 문제풀이용 ###
from collections import deque
def solution(h,n,m,board):
    countBad = 0
    for x in range(m):
        for y in range(n):
            for z in range(h):
                if board[x][y][z] == 0:
                    countBad += 1
    #익혀야할 토마토가 없으면 = 다 익은 토마토이면
    if countBad == 0:
        return 0
    
    #익힌 토마토 수
    #숙성시키자!
                
    q = deque()
    for x in range(m):
        for y in range(n):
            for z in range(h):
                if board[x][y][z] == 1:
                    q.append((x,y,z,0))
    answer = 0
    while q:
        cx, cy, cz, cday = q.popleft()
        answer = max(answer, cday)
        for dx, dy, dz in [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]:
            nx, ny, nz = cx + dx, cy + dy, cz + dz
            if 0<=nx<m and 0<=ny<n and 0<=nz<h:
                if board[nx][ny][nz] == 0:
                    board[nx][ny][nz] = 1
                    q.append((nx, ny, nz, cday + 1))

        
    #익히지 못한 토마토가 존재하면
    for x in range(m):
        for y in range(n):
            for z in range(h):
                if board[x][y][z] == 0:
                    return -1

    return answer
    
        
### 입력 ###
m,n,h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
print(solution(m,n,h,board))
