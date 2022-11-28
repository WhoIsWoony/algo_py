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
import copy

### 문제풀이용 ###
from collections import deque
def solution(n,m,board):
    
    def countSafe(boardAfterSpread):
        cnt = 0
        for r in range(n):
            for c in range(m):
                if boardAfterSpread[r][c] == 0:
                    cnt += 1
        return cnt

    def spreadVirus(boardWithWall):
        for r in range(n):
            for c in range(m):
                if boardWithWall[r][c] == 2:
                    q = deque()
                    q.append((r,c))
                    while q:
                        cr, cc = q.popleft()
                        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nr, nc = cr + dr, cc + dc
                            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                                continue
                            if boardWithWall[nr][nc] == 0:
                                boardWithWall[nr][nc] = 2
                                q.append((nr, nc))

        return boardWithWall

    answer = 0
    for i in range(0, n*m-2):
        for j in range(i+1, n*m-1):
            for z in range(j+1, n*m):
                w1r, w1c = i//m, i%m
                w2r, w2c = j//m, j%m
                w3r, w3c = z//m, z%m
                if board[w1r][w1c]==0 and board[w2r][w2c]==0 and board[w3r][w3c]==0:
                    boardCopy = copy.deepcopy(board)
                    boardCopy[w1r][w1c],boardCopy[w2r][w2c],boardCopy[w3r][w3c] = 1,1,1
                    virusBoard = spreadVirus(boardCopy)
                    safeArea = countSafe(virusBoard)
                    answer = max(safeArea, answer)
    return answer
    

### 입력 ###
n, m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
print(solution(n,m,board))
