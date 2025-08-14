from collections import deque
from itertools import permutations

n = int(input())
seq = "abcdefghijklmn"
main_track = ""
for char in range(n):
    main_track += seq[char]
# print(main_track)


# def func(start, end):
#     start_index = {char: i for i, char in enumerate(start)}
    
#     dest_list = list(end)

#     swaps = 0

#     for i in range(len(end)):
#         if dest_list[i] != start[i]:
#             correct_index = start_index[dest_list[i]]
#             dest_list[i], dest_list[correct_index] = dest_list[correct_index], dest_list[i]

#             swaps += 1

#     return swaps


def bfs(arash):
    qu = deque()
    first_level = 0
    qu.append({"seq":main_track, "lev":first_level})
    # queue = []
    # queue.append((main_track, first_level))
    # marked = set()
    cnt = -1
    # dist = {}
    # dist[start_permutation] = 0
    while qu:
    # while len(queue) != 0:
        # print(len(qu))
        # current_permutation, current_level = qu.popleft()
        seq_item = qu.popleft()
        # current_permutation, current_level = queue.pop(0)
        # print("cur", current_permutation)
        # marked.add((current_permutation))
        # print("-", current_permutation, current_level)
        # for x in range(1, len(start_permutation) + 1):
        # changed_permutation = start_permutation[0:x][::-1] + start_permutation[x:]
        if not (arash[seq_item["seq"]] != -5):
            arash[seq_item["seq"]] = seq_item["lev"]
            for x in range(n):
                for y in range(x + 1, n):
                    changed_perm = seq_item["seq"][0:x] + seq_item["seq"][x:y+1][::-1] + seq_item["seq"][y+1:]
                    # print("*", changed_perm, current_level + 1)
                    qu.append({"seq":changed_perm,"lev": seq_item["lev"]+1})
                    # queue.append((changed_perm, current_level+1))
                    # if chan not in marked:
                        # qu.append((chan, current_level + 1))
                        # marked.add(chan)
                        # dist[current_permutation] = current_level + 1
        # else:
        #     arash[current_permutation] = 1
        # cnt += 1

        # if (current_permutation) not in marked:
        #     dist[current_permutation] = current_level
        #     for i in range(n):
        #         for j in range(i+1, n):
        #             changed_one = current_permutation[0:i][::-1] + current_permutation[i:j+1] + current_permutation[j+1:]
                    
        #             print("changed", changed_one)
        #             changed_level = current_level+1
        #             qu.append((changed_one, changed_level))
                    
            # qu.append((changed_permutation, dist[changed_permutation]))
            # marked.add(current_permutation)
    # print("return before", arash)
    return arash

elemetns = permutations(main_track)
# print(elemetns)
arash = {}
for perm in elemetns:
    arash["".join(list(perm))] = -5
# print(arash)
# print('\n'.join(str(permutation) for permutation in obj))

# print(len(arash.keys()))

# lst = []
# for i in arash.keys():
#     lst.append(i)

tree = bfs(arash)
# print(tree)
t = int(input())

mamad = {}
lst = []
result = [""] * t
for babak in range(t):
    start_permutation_str, destination_order_str = map(str, input().split())
    # if start_permutation_str == main_track:
    #     # lst.append(tree[destination_order_str])
    #     # print(tree[destination_order_str])
        
    #     # print("mahdi")
    #     continue
    ans = ""
    for i in range(n):
        mamad[start_permutation_str[i]] = main_track[i]
    for j in range(n):
        ans = ans + mamad[destination_order_str[j]]
    result[babak] = ans
    # lst.append(tree[ans])
    # print(tree[ans])
# {'abc': 1, 'acb': 1, 'bac': 1, 'bca': 2, 'cab': 2, 'cba': 1}
for i in range(t):
    print(tree[result[i]])