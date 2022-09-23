#오후 12:45 시작
#

bonus={
    'S':1,
    'D':2,
    'T':3
}

def solution(dartResult):
    answer = 0
    round = 0

    pointPrev = 0
    pointNow = 0
    
    while(round < 2):
        if dartResult[1] in bonus:
            pointNow = int(dartResult[0]) ** bonus[dartResult[1]]
            dartResult = dartResult[2:]
        else:
            pointNow = 10 ** bonus[dartResult[2]]
            dartResult = dartResult[3:]
        
        if dartResult[0]=='*': 
            pointNow = pointNow * 2
            pointPrev = pointPrev * 2
            dartResult = dartResult[1:]
        elif dartResult[0]=="#":
            pointNow = pointNow * -1
            dartResult = dartResult[1:]

        answer = answer + pointPrev
        pointPrev = pointNow
        round = round+1

    if dartResult[1] in bonus:
        pointNow = int(dartResult[0]) ** bonus[dartResult[1]]
        dartResult = dartResult[2:]
    else:
        pointNow = 10 ** bonus[dartResult[2]]
        dartResult = dartResult[3:]
    if len(dartResult)>0:
        if dartResult[0]=='*': 
            pointNow = pointNow * 2
            pointPrev = pointPrev * 2
            dartResult = dartResult[1:]
        elif dartResult[0]=="#":
            pointNow = pointNow * -1
            dartResult = dartResult[1:]
    answer = answer + pointNow + pointPrev

    return answer


print(solution("1D2S#10S"))