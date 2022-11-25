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
def solution(a,b,c):
    def power(a, b):
        if b == 1: # b의 값이 1이면 a % C를 return한다.
            return a % c
        else:
            temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
            if b % 2 == 0:
                return temp * temp % c # b가 짝수인 경우
            else:
                return temp * temp * a % c # b가 홀수인 경우
    return power(a,b)
        

### 입력 ###
a,b,c = map(int, input().split())
print(solution(a,b,c))
