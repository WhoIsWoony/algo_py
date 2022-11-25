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
def solution(target, broken):
    minCnt = abs(100 - target)

    for nums in range(1000001):
        nums = str(nums)
        for j in range(len(nums)):
            # 각 숫자가 고장났는지 확인 후, 고장 났으면 break
            if int(nums[j]) in broken:
                break
            # 고장난 숫자 없이 마지막 자리까지 왔다면 min_count 비교 후 업데이트
            elif j == len(nums) - 1:
                minCnt = min(minCnt, abs(int(nums) - target) + len(nums))
        
    return minCnt

### 입력 ###
target = int(input())
n = int(input())
broken = [] if n == 0 else list(map(int, input().split()))
print(solution(target, broken))
