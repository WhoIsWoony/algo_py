def solution(s):
    answer = ''
    mid = int(len(s)/2)
    if(len(s)%2==1):
        answer = s[mid]
    else:
        answer = s[mid-1]+s[mid]
    return answer