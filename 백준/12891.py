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
check = 0
def solution(S, P, DNA, A,C,G,T):
    CNT = {
        "A":DNA[:P].count("A"),
        "C":DNA[:P].count("C"),
        "G":DNA[:P].count("G"),
        "T":DNA[:P].count("T")
    }

    def check():
        if A <= CNT["A"] and C <= CNT["C"] and G <= CNT["G"] and T <= CNT["T"]:
            return True
        return False

    answer = 1 if check() else 0
    
    i = 0
    while i+P < S:
        ascDel = DNA[i]
        ascNew = DNA[i+P]
        CNT[ascDel] -= 1
        CNT[ascNew] += 1
        if check():
            answer += 1
        i += 1

    return answer;
###############

### 입력, 결과 ###
S, P = map(int,input().split())
DNA = input()
A,C,G,T = map(int, input().split())
#print(solution(N), checkAnswer(sol))   #체크용
print(solution(S, P, DNA, A,C,G,T))                 #풀이용
###############
