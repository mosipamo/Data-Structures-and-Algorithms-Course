N, B = map(int, input().split())
fi = list(map(int, input().split()))
vals = []
for i in range(N) :
    vals.append((fi[i], i))

vals.sort(reverse=True)
# print(vals)

PS = []
for _ in range(B):
    p, q = map(int, input().split())
    # print(p, q, _)
    PS.append((p, q, _))
    
PS.sort(reverse= True)
# print(PS)

par = [i for i in range(N)]
val = [0] * N
mark = [1] * N

mx = 0
# print(par)

def get(v) : 
    if(v == par[v]) : 
        return v
    par[v] = get(par[v])
    return par[v]

def merge(u, v) :
    global mx
    # print(" => ", u, v)
    u = get(u)    
    v = get(v)
    # print(" =>** ", u, v)
    
    par[u] = v
    val[v] += val[u]
    
    mx = max(mx, val[v])

ans = [0] * B

idx = 0
for i in range(B) : 
    x = PS[i][0]
    while(idx < N and vals[idx][0] > x) :
        # print("ridi : ", x, idx, i)
        ind = vals[idx][1]
        val[ind] += 1
        mx = max(mx, val[ind])
        
        mark[ind] = 0
        if(ind + 1 < N) : 
            if(mark[ind + 1] == 0) : 
                merge(ind, ind + 1)
        
        if(ind - 1 >= 0) :
            if(mark[ind - 1] == 0) : 
                merge(ind, ind - 1)
        
        idx += 1
    
    # print("=>", mx)
    if(mx >= PS[i][1]) : 
        ans[PS[i][2]] = 0
    else : 
        ans[PS[i][2]] = 1
            
for i in range(B) : 
    print(ans[i])