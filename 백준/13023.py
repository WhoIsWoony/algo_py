import sys
import math
#sys.setrecursionlimit(10000)
sys.stdin = open("./input.txt", "r")
#input = sys.stdin.readline

### 정답체크용 ###
"""
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
###############

### 문제풀이용 ###
def solution(N, M, graph):
    return 0
###############

### 입력, 결과 ###
N, M = map(int,input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(solution(N), checkAnswer(sol)) #체크용
print(solution(N, M, graph))          #풀이용
###############
