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
def solution(n, s, arr):
    l, r = 0, 0;
    amount = arr[0]
    count = 1
    answer = 0
    while r < n-1:
        #r을 높여서 기준값을 통과 가능하도록 노력
        if amount < s:
            r += 1
            count += 1
            amount += arr[r]
        #기준값 통과시 저장하고 l을 높임
        elif amount >= s:
            if answer == 0:
                answer = count
            else:
                answer = min(answer, count)
            amount -= arr[l]
            l += 1
            count -= 1

    while amount >= s:
        if answer == 0:
            answer = count
        else:
            answer = min(answer, count)
        amount -= arr[l]
        l += 1
        count -= 1
    
    return answer
    
        
### 입력 ###
n,s = map(int, input().split())
arr = list(map(int, input().split()))
print(solution(n, s, arr))
