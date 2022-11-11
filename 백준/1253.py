import sys
#sys.stdin = open("./input.txt", "r")
input = sys.stdin.readline

### 정답체크용 ###
"""
answer = open("./output.txt", "r")
def checkAnswer(sol):
    return sol == answer.readline().strip()
"""
###############


### 문제풀이용 ###
def solution(N, arr):
    #arr[i] = arr[j] + arr[z] i는 GOOD
    #arr은 절대 값이 1,000,000,000 이하인 정수 배열
    arr.sort()
    answer = 0
    
    for i in range(N):
        tmp = arr[:i] + arr[i+1:]
        left, right = 0, len(tmp)-1;
        while left < right:
            sum = tmp[left] + tmp[right]
            if sum == arr[i]:
                answer += 1
                break
            elif sum < arr[i]: left += 1
            elif sum > arr[i]: right -= 1
    return answer;
###############

### 입력, 결과 ###
N = int(input())
arr = list(map(int, input().split()))
#print(solution(N), checkAnswer(sol))   #체크용
print(solution(N, arr))                 #풀이용
###############
