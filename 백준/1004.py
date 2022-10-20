import enum
from math import sqrt
import sys
input = sys.stdin.readline

T = int(input())

def checkDotInCircle(x,y,cicleInfo):
    cx, cy, r = cicleInfo
    return (x-cx)**2 + (y-cy)**2 < r**2

for t in range(T):
    x1, y1, x2, y2 = map(int, input().split(" "))
    n_planet = int(input())
    planet = []
    for n in range(n_planet): 
        cx, cy, r = map(int, input().split(" "))
        planet.append((cx, cy, r))
        
    delCount = 0 
    for i, circleInfo in enumerate(planet):
         if (checkDotInCircle(x1, y1, circleInfo) and checkDotInCircle(x2, y2, circleInfo)) or (not checkDotInCircle(x1, y1, circleInfo) and not checkDotInCircle(x2, y2, circleInfo)):
            delCount+=1
    print(len(planet)-delCount)