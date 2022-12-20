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
sys.setrecursionlimit(10**6)            #Tip3 : 파이썬 재귀함수 에러 방지, 백준에서 유용
INF = int(1e9)
    
### 문제풀이용 ###
def solution(n, prices):
    answer, standard = 0, 0
    for i in range(len(prices)-1, -1, -1):
        #마지막으로 가장 컸었던 주식보다 작으면, 
        if prices[i] < standard:
            answer += (standard - prices[i])
        else:
            standard = prices[i]
    return answer

### 입력 ###
T = int(input())
for t in range(T):
    n = int(input())
    prices = list(map(int, input().split()))
    print(solution(n, prices))