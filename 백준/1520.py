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
def solution(n, m, board):
    dp = [[-1]*m for _ in range(n)]
    def dfs(cr,cc):
        if cr == n-1 and cc == m-1: 
            return 1
        if dp[cr][cc] == -1:
            dp[cr][cc] = 0
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = cr+dr, cc+dc
                if 0 <= nr < n and 0 <= nc < m:
                    if board[nr][nc] < board[cr][cc]:
                        dp[cr][cc] += dfs(nr, nc)
        return dp[cr][cc]
    
        
    return dfs(0,0)
    
        
### 입력 ###
n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, board))
