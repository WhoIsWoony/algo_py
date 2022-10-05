def timeDiff(t1, t2):
    h1, m1 = map(int, t1.split(":"))
    h2, m2 = map(int, t2.split(":"))
    return (h2 * 60 + m2) - (h1 * 60 + m1)

def solution(fees, records):
    cars = {}
    amount = {}
    for car in records:
        time, num, io = car.split(" ")
        if num not in cars:
            cars[num] = time
        else:
            if num not in amount:
                amount[num] = 0
            amount[num] += timeDiff(cars[num], time)
            del cars[num]
            
    for k,v in cars.items():
        if k not in amount:
            amount[k] = 0
        amount[k] += timeDiff(v, "23:59")
        
    answer = []
    for k,v in sorted(amount.items()):
        print(k,v)
        if v < fees[0]:
            answer.append(fees[1])
        else:
            v -= fees[0]
            cost = fees[1]
            cost += int(v/fees[2]) * fees[3]
            if v%fees[2] > 0:
                cost += fees[3]
            answer.append(cost)

    return answer
    
solution([180, 5000, 10, 600],	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
