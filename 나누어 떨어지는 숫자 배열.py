def solution(arr, divisor):
    answer = set([])
    for i in arr:
        if(i % divisor == 0):
            answer.update([i])
    answer = list(answer)
    answer.sort()
    return answer if len(answer) > 0 else [-1]