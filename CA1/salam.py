def check_friends_availability(l, r, p):
    if l[:2] == '12':
        l = '00' + l[2:]
    if r[:2] == '12':
        r = '00' + r[2:]
    if p[:2] == '12':
        p = '00' + p[2:]
    
    # print(l, p, r)
    
    if l[6:] == p[6:] == 'AM':
        if l[:5] <= p[:5]:
            if r[6:] == 'AM':
                if p[:5] <= r[:5]:
                    return 1
                return 0
            else:
                return 1
            
        return 0
    
    if l[6:] == p[6:] == 'PM':
        if l[:5] <= p[:5]:
            if r[6:] == 'PM':
                if p[:5] <= r[:5]:
                    return 1
                return 0
            else:
                return 1
        return 0
    
    
    if l[6:] == 'AM' and p[6:] == 'PM':
        if r[6:] == 'AM':   
            return 0
        else:
            if p[:5] <= r[:5]:
                return 1
            return 0
        
    if l[6:] == 'PM' and p[6:] == 'AM':
        if r[6:] == 'PM':
            return 0
        else:
            return 1
    

t = int(input())
res = []

for _ in range(t):
    p = input()    # time for meeting
    n = int(input())    # count of friends


    for _ in range(n):
        friend_range = input().split()
        Li = friend_range[0] + ' ' + friend_range[1]
        Ri = friend_range[2] + ' ' + friend_range[3]
        ans = check_friends_availability(Li, Ri, p)
        res.append(ans)
    res.append('\n')
        
for t in res:
    print(t, end='')