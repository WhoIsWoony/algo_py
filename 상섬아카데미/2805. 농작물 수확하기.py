#오후 12:20 시작
#오후 01:04 종료
import sys
sys.stdin = open("./input.txt", "r")

### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
### 정답체크용 ###
    
def solution(N, FARM):
    answer = 0
    for r in range(int(N/2)):
        s = int(N/2) - r
        e = int(N/2) + r
        for c in range(s, e+1):
            #print(int(FARM[r][c]), end="")
            answer += int(FARM[r][c])
        #print()
    for c in range(N):
        #print(int(FARM[int(N/2)][c]), end="")
        answer += int(FARM[int(N/2)][c])
    #print()

    for r in range(int(N/2)+1, N):
        s = int(N/2) - (N-1-r)
        e = int(N/2) + (N-1-r)
        for c in range(s, e+1):
            #print(int(FARM[r][c]), end="")
            answer += int(FARM[r][c])
        #print()

    return answer

for t in range(1, int(input())+1):
    N = int(input())
    FARM = [input() for _ in range(N)]
    sol = f"#{t} {solution(N, FARM)}"
    #체크용
    #print(sol, checkAnswer(sol))
    #제출용
    print(sol)
    
