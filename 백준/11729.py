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
def solution(n):
    # 입력: 옮기려는 원반의 갯수 n
    #      옮길 원반이 현재 있는 출발점 기둥 from_pos
    #      원반을 옮길 도착점 기둥 to_pos
    #      옮기는 과정에서 사용할 보조 기둥 aux_pos
    global m
    m = 0
    log=[]
    def hanoi(n, from_pos, to_pos, aux_pos):
        global m 
        if n == 1:  # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
            log.append((from_pos, to_pos))
            m += 1
            return
        # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
        hanoi(n - 1, from_pos, aux_pos, to_pos)
        # 가장 큰 원반을 목적지로 이동
        log.append((from_pos, to_pos))
        m += 1
        # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
        hanoi(n - 1, aux_pos, to_pos, from_pos)
    hanoi(n, 1, 3, 2)

    
    print(m)
    for from_pos, t_pos in log:
        print(from_pos, t_pos)
    

### 입력 ###
n = int(input())
solution(n)
