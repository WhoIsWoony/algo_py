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
def solution(n,k,items):
    dp = [0]*(k+1)

    for w, v in items:
        if w > k:
            continue
        #7 6 5 4 3 2 1
        for i in range(k,0,-1):
            #7+w 6+w 5+w 4+w 3+w 2+w 1+w
            #dp[i] != 0
            if i+w <= k and dp[i] != 0:
                #이전 i 무게의 최대값과 더했을 시 무게의 가치의 최대값
                dp[i+w] = max(dp[i+w], dp[i] + v)
        dp[w] = max(dp[w], v)
    return(max(dp))

### 입력 ###
n, k = map(int, input().split())
items = []
for _ in range(n): 
    m, v = map(int, input().split())
    items.append((m,v))
print(solution(n,k,items))
