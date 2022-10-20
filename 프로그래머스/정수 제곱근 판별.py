import math
#import sys
#fastread = sys.stdin.readline

def solution(n):
    sr = math.sqrt(n)
    if(sr % 1 == 0):
        return (sr+1)*(sr+1)
    else: 
        return -1