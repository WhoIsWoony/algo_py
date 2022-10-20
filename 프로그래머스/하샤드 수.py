def solution(x):
    sum = 0
    iter = x
    while iter > 0:
        sum += iter%10
        iter = int(iter/10)
    return x%sum==0