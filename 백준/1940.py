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
def solution(N, M, irons):
    #iros들의 두 수를 합쳐서 M이 되면 갑옷 완성
    #만들 수 있는 갑옷 수 반환
    #iron에 겹치는 수는 없음
    
    answer = 0
    irons = sorted(irons);
    front, back = 0, N-1
    while front != back:
        sum = irons[front] + irons[back];
        if sum == M:
            answer += 1
            back -= 1
        elif sum > M:
            back -= 1
        elif sum < M:
            front += 1
    
    return answer;
###############

### 입력, 결과 ###
N = int(input())
M = int(input())
irons = list(map(int, input().split()))
#print(solution(N), checkAnswer(sol))   #체크용
print(solution(N, M, irons))                      #풀이용
###############
