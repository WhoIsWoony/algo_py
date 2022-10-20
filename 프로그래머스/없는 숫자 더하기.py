def solution(numbers):
    defaultSet = set([0,1,2,3,4,5,6,7,8,9])
    numberSet = set(numbers)
    
    differSet = list(defaultSet-numberSet)
    
    answer = 0
    for i in differSet:
        answer += i

    return answer