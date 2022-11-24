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
def solution(r, c, board):
    global answer
    answer = 0

    q = set([(0, 0, board[0][0])])
    while q:
        cr, cc, history = q.pop()
        answer = max(answer, len(history))
        for dr, dc in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr and nr < r and 0 <= nc and nc < c:
                if board[nr][nc] not in history:
                    q.add((nr, nc, board[nr][nc] + history))

    return answer

### 입력 ###
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
print(solution(r, c, board))
