import sys
sys.setrecursionlimit(10000)
sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline


"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
### 문제풀이용 ###
def solution(n, wines):
    dp = [0]
    dp.append(wines[1])
    if n > 1:
        dp.append(wines[1] + wines[2])
    for i in range(3, n+1):
        dp.append(max(dp[i - 1], dp[i - 3] + wines[i - 1] + wines[i], dp[i - 2] + wines[i]))
    return dp[n]

### 입력 ###
n = int(input())
wines = [0]+[int(input()) for _ in range(n)]

### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
print(solution(n, wines))                        #풀이용
