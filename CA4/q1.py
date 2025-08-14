n, m = map(int, input().split())


class1 = []
class2 = []

v, u = map(int, input().split())

class1.append(v)
class2.append(u)
seen = []
seen.extend([v, u])

for i in range(m - 1):
    v, u = map(int, input().split())
    
    if v in seen and u in seen:
        continue
    
    elif v in seen:
        if v in class1:
            class2.append(u)  
            seen.append(u)
        if v in class2:
            class1.append(u)
            seen.append(u)
    
    elif u in seen:
        if u in class1:
            class2.append(v)
            seen.append(v)
        if u in class2:
            class1.append(v)
            seen.append(v)
        
    
    elif v not in seen and u not in seen:
        class1.append(v)
        class2.append(u)
        seen.extend([v, u])

print(len(class1))
print(*class1)
    