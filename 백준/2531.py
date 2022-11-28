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
def solution(n,d,k,c,belt):
    #회전일반화
    belt = belt+belt[0:k-1]
    
    #메뉴별 카운트
    count = {}
    for menu in range(1, d+1):
        count[menu] = 0

    #초기값
    cnt = 0
    for sushi in belt[0:k]:
        count[sushi]+=1
        if count[sushi] == 1:
            cnt += 1

    #O(n) 투포인터 진행
    answer = 0
    for i in range(0, len(belt)-k):
        l, r = i, i+k
        count[belt[l]] -= 1
        if count[belt[l]] == 0:
            cnt -= 1

        count[belt[r]] += 1
        if count[belt[r]] == 1:
            cnt += 1
        #쿠폰의 스시 존재 여부
        if count[c]==0:
            answer = max(answer, cnt + 1)
        else:
            answer = max(answer, cnt)
    return answer 

### 입력 ###
# 2 ≤ n ≤ 30,000
# 2 ≤ d ≤ 3,000
# 2 ≤ k ≤ 3,000 (k ≤ N)
# 1 ≤ c ≤ d
n,d,k,c = map(int,input().split())
belt = [int(input()) for _ in range(n)]
print(solution(n,d,k,c,belt))
