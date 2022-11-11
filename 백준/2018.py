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
def solution(N):
    case = 1;
    sum = 1
    p_front, p_back = 1, 1;
    while p_back != N:
        if sum == N: 
            case += 1
            p_back += 1
            sum += p_back
        elif sum > N:
            sum -= p_front
            p_front += 1
        elif sum < N:
            p_back += 1
            sum += p_back

    return case;
###############

### 입력, 결과 ###
N = int(input())
#print(solution(N), checkAnswer(sol))   #체크용
print(solution(N))                      #풀이용
###############
