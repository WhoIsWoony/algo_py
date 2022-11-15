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

#8
#2, 6 = 3 * 2
#6, 2 = 3 * 2
#2, 4, 2 
#2, 2, 4
#4, 2, 2
#2, 2, 2, 2

### 문제풀이용 ###
def solution(N):
    if N%2 == 1: return 0
    
    dp = [0 for _ in range(31)]
    dp[2] = 3
    for i in range(4, N+1, 2):
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2

    return dp[N]
###############

### 입력, 결과 ###
N = int(input())

#print(solution(N), checkAnswer(sol)) #체크용
print(solution(N))          #풀이용
###############
