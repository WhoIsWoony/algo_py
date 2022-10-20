from math import sqrt
import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
    #두 터렛 사이의 거리
    distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
    #발견한 위치의 거리 합
    rp = r1 + r2
    #발견한 위치의 거리 차
    rm = abs(r1 - r2)


    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == rp or distance == rm:
        print(1)
    elif rm < distance < rp:
        print(2)
    else:
        print(0)
    