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
import math
def solution(n):
    # 소수 판별
    def isPrimeNumber(x):
        for i in range(2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
            if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
                return False
        return True				# 전부 나눠떨어지지 않는다면 소수임

    for i in range(2, int(n/2)+1):
        if isPrimeNumber(i) and isPrimeNumber(n-i):
            return f"{n} = {i} + {n-i}"

    return "Goldbach's conjecture is wrong."
    
        
### 입력 ###
while True:
    n = int(input())
    if n == 0: break
    print(solution(n))