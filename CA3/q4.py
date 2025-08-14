parents_dict = {}
children_count_dict = {}
n, q = map(int, input().split())
parents = list(map(int, input().split()))

parents_dict = {i+2:parents[i] for i in range(n - 1)}
parents_dict[1] = None

children_count_dict = {i+1:0 for i in range(n)}

for i in range(n - 1):
    children_count_dict[parents[i]] += 1

Queries_list = []
for i in range(q):
    a, *b = (list(map(int, input().split())))
    Queries_list.append(b)

for qu in Queries_list:    
    res = 0
    parent_count = {parents_dict[i]: 0 for i in qu}
    for n in qu:
        res += children_count_dict[n] + 1
        
        if parents_dict[n] is not None:
            parent_count[parents_dict[n]] += 1
    for i in qu:
        if i in parent_count.keys():
            res -= 2 * parent_count[i]

    print(res)