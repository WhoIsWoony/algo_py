def solution(phone_number):
    listStr = list(phone_number)
    for i in range(0,len(listStr)-4):
        listStr[i] = '*'
    return ''.join(listStr)