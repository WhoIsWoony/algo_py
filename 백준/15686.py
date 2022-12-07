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
from itertools import combinations
def solution(n, m, board):
    chickens = []
    houses = []

    #치킨집과 집들의 좌표 저장
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                houses.append((r,c))
            elif board[r][c] == 2:
                chickens.append((r,c))

    answer = float('inf')
    for combi in combinations(chickens, m):
        total_distance = 0
        for r1, c1 in houses:   
            distance = float('inf')
            #각 집과 뽑은 치킨집들 사이 최소거리를 구한다.
            for r2, c2 in combi:
                distance = min(distance, abs(r1 - r2) + abs(c1 - c2))
            #도시최소거리 반영
            total_distance += distance
        #결과 반영
        answer = min(answer, total_distance)

    return answer
    
        
### 입력 ###

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, board))
