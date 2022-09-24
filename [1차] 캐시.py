from calendar import c
from collections import deque
from queue import PriorityQueue


def solution(cacheSize, cities):
    cost = 0
    cache = [""]*cacheSize

    cost = 0
    for city in cities:
        idx = -1
        for i, c in enumerate(cache):
            if(c == city.upper()):
                idx=i
                break

        if idx == -1:
            cost += 5
            cache.insert(0, city.upper())
            cache.pop()
        else:
            cost += 1
            temp = cache[idx]
            del cache[idx]
            cache.insert(0, temp)
    return cost

#solution(3,	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])