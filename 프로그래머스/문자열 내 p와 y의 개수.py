def solution(s):
    n_p = 0
    n_y = 0
    for i in s:
        if(i=="p" or i=="P"):
             n_p += 1
        elif(i=="y" or i=="Y"):
             n_y += 1
        
    return (n_p==0 and n_y==0) or (n_p==n_y)