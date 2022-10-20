def solution(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    del arr[arr.index(min)]

    return [-1] if len(arr) == 0 else arr