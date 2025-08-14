n = int(input())
# h=[]
houses = []
for i in range(n):
    num = int(input())
    # h.append(num)
    houses.append((i, num))

colors_range = {}
for i in range(len(houses)):
    if houses[i][1] not in colors_range:
        colors_range[houses[i][1]] = [i, i]    
    if houses[i][1] in colors_range:
        colors_range[houses[i][1]][1] = i
        

def split_sequence_by_zero(sequence):
    subsequences = []
    current_subsequence = []

    for num in sequence:
        if num[1] == 0:
            if current_subsequence:
                subsequences.append(current_subsequence.copy())
                current_subsequence = []
        else:
            current_subsequence.append(num)

    if current_subsequence:
        subsequences.append(current_subsequence.copy())

    return subsequences


mamad = split_sequence_by_zero(houses)

ans=0
stack = []
for sub in mamad:
    impossible = False
    for k in range(len(sub)):
        if sub[k][0] == colors_range[sub[k][1]][0]:
            stack.append(sub[k][1]) 
            if(len(stack) > ans):
                ans = len(stack)
            if sub[k][0] == colors_range[sub[k][1]][1]:
                stack.pop()
        elif sub[k][0] == colors_range[sub[k][1]][1]:
            if stack[-1] == sub[k][1]:
                stack.pop()
            else:
                impossible = True
                break
    if len(stack) > 0 or impossible is True:
        ans = -1
        break
print(ans)