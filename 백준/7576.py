import sys
#sys.setrecursionlimit(10000)
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
def solution(m, n, tomatos):
    day = 0

    maxCanEat = 0
    q = deque()
    for r in range(n):
        for c in range(m):
            if tomatos[r][c] == 1: 
                q.append((r,c, day))
            if tomatos[r][c] != -1:
                maxCanEat += 1

    canEat = 0
    while q:
        cr, cc, cd = q.popleft()
        day = cd
        canEat += 1
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m and tomatos[nr][nc] == 0:
                tomatos[nr][nc] = 1
                q.append((nr, nc, day + 1))
    

    return day if canEat == maxCanEat else -1

### 입력 ###
m, n = map(int,input().split())
tomatos = [list(map(int, input().split())) for _ in range(n)]

### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
print(solution(m, n, tomatos))                        #풀이용
