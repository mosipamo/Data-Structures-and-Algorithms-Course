n = int(input())
y = list(map(int, input().split()))


pos = {} # positions of inputs   # pos[i]: i->value-key  pos[i]->جایگاه
for i in range(0, n):
    pos[y[i]] = i
# print(pos)

prev_stack = []
prev_pos = {}


for i in range(n, 0, -1):
    while (prev_stack):
        if pos[prev_stack[-1]] < pos[i]:
            prev_pos[pos[i]] = pos[prev_stack[-1]]
            break
        elif pos[prev_stack[-1]] > pos[i]:
            prev_stack.pop()
        
    prev_stack.append(i)
    
# print(prev_stack)
# print(prev_pos)
    
    
res = 0
stack = []
for i in range(1, n+1):
    print(res)
    while stack:
        if stack[-1] > pos[i]:
            stack.pop()
            res -= 1
        else:
            break
    flag = False
    if pos[i] in prev_pos.keys():
        if not stack:
            flag = True
        elif prev_pos[pos[i]] != prev_pos[stack[-1]]:
            flag = True
        else:
            flag = False
    if flag:
        stack.append(pos[i])
        res += 1
print(res)
        
        

        