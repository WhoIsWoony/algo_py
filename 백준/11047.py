import sys
sys.setrecursionlimit(10000)
sys.stdin = open("./input.txt", "r")
#input = sys.stdin.readline

"""
### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""


### 문제풀이용 ###
def solution(N,K,values):
    answer = 0
    for value in values:
        if K >= value:
            answer += K // value
            K %= value
            if K <= 0:
                break
            
    return answer

### 입력 ###
N,K = map(int, input().split())
values = []
for _ in range(N):
    values.insert(0, int(input()))

### 출력 ###
#print(solution(N), checkAnswer(sol)) #체크용
print(solution(N,K,values))                        #풀이용
