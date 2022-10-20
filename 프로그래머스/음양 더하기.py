def solution(absolutes, signs):
    answer = 0
    
    for i in range(0, len(absolutes)):
        answer += (1 if signs[i] else -1) * absolutes[i]
    
    return answer