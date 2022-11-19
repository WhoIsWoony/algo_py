import sys
sys.stdin = open("./input.txt", "r")

### 정답체크용 ###
answer = open("./output.txt", "r")
def checkAnswer(sol):
    read = answer.readline().strip()
    print(f"sol:{sol}, answer:{read}, result:{sol == read}")

### 문제풀이용 ###
def solution(maxDump, boxList):
    boxList.sort()
    numDump = 0
    diff = 0
    while numDump <= maxDump:
        diff = boxList[-1] - boxList[0]
        if diff == 1 or diff == 0: break
        
        boxList[0]+=1
        boxList[-1]-=1

        idx = -1
        while boxList[idx-1] > boxList[idx]:
            boxList[idx-1], boxList[idx] = boxList[idx], boxList[idx-1]
            idx -= 1

        idx = 0
        while boxList[idx+1] < boxList[idx]:
            boxList[idx+1], boxList[idx] = boxList[idx], boxList[idx+1]
            idx += 1

        numDump += 1
    return diff

### 입력, 결과 ###
for t in range(1, 11):
    maxDump = int(input())
    boxList = list(map(int, input().split()))
    
    #checkAnswer(f"#{t} {solution(maxDump, boxList)}")   #체크용
    print(f"#{t} {solution(maxDump, boxList)}")          #풀이용
