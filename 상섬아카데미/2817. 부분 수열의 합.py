#오후 02:30 시작
#오후 01:04 종료
import sys
sys.stdin = open("./input.txt", "r")

### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
###############

### 문제풀이용 ###
def solution(N,K,A):

    def dfs(idx, sum):
        global answer
        if idx >= N:
            return
        if sum + A[idx] == K:
            answer += 1
        dfs(idx+1, sum)
        dfs(idx+1, sum + A[idx])
    dfs(0,0)

    return answer
###############

### 입력, 결과 ###
for t in range(1, int(input())+1):
    answer = 0
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sol = f"#{t} {solution(N,K,A)}"
    #print(sol, checkAnswer(sol))   #체크용
    print(sol)                      #풀이용
###############
