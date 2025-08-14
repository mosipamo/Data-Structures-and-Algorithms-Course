import heapq
n, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

angers = 0
for teacher in data:
    angers += teacher[1] * teacher[2] 

data.sort(key=lambda x: x[0])
max_heap = []

s = 0
j = 0
for day in range(1, d + 1):
    while len(data) != j and data[j][0] <= day:
        heapq.heappush(max_heap, [-1 * data[j][2], data[j][1]])
        j += 1
    if not max_heap:
        continue
    
    max_heap[0][1] -= 1
    s += -max_heap[0][0]
    if max_heap[0][1] == 0:
        heapq.heappop(max_heap)
        
res = angers - s
print(res)