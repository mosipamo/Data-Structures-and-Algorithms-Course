n = int(input()) 
final_res_count = 2 * n - 2

def build_tree(input_list):
    tree = {}
    for parent, child in input_list:
        if parent not in tree:
            tree[parent] = {"parent": None, "children": []}
        tree[child] = {"parent": parent, "children": []}
        tree[parent]["children"].append(child)
    return tree
height = {i + 1: 0 for i in range(n)}

nodes = []
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    nodes.append((u, v))
    height[v] = height[u] + 1

tree = build_tree(nodes)
tree["height"] = height

leaves = list(map(int, input().split()))

def find_lca(tree, node1, node2):
    visited = set()
    while node1 is not None or node2 is not None:
        if node1 is not None:
            if node1 in visited:
                return node1
            visited.add(node1)
            node1 = tree[node1]["parent"]
        if node2 is not None:
            if node2 in visited:
                return node2
            visited.add(node2)
            node2 = tree[node2]["parent"]
    return None

    
def start_root(leaf):
    lst = []
    while leaf != 1:
        lst.append(leaf)
        leaf = tree[leaf]["parent"]
    lst.append(1)
    lst.reverse()
    lst.pop()
    return lst

def start_from_leaf(leaf, lca_found):
    lst = []
    while leaf != lca_found:
        lst.append(leaf)
        leaf = tree[leaf]["parent"]
    return lst

def start_from_seen_leaf(leaf, lca_found):
    lst = []
    while leaf != lca_found:
        lst.append(leaf)
        leaf = tree[leaf]["parent"]
    lst.pop(0)
    return lst

ways = []
arash = []
seen = []

leaf1 = leaves[0]
arash = start_root(leaf1)
ways.extend(arash)

for i in range(len(leaves) - 1):
    leaf1 = leaves[i]
    leaf2 = leaves[i + 1]
    
    lca_found = find_lca(tree,leaf1, leaf2)
    leaf1_list = []
    if leaf1 not in seen:
        leaf1_list = start_from_leaf(leaf1, lca_found)
    else:
        leaf1_list = start_from_seen_leaf(leaf1, lca_found)
    ways.extend(leaf1_list)
    
    leaf2_list = []
    leaf2_list = start_from_leaf(leaf2, lca_found)
    leaf2_list.append(lca_found)
    leaf2_list.reverse()
    
    ways.extend(leaf2_list)
    seen.append(leaf1)
    seen.append(leaf2)

left = []
left = start_from_seen_leaf(leaves[-1], 1)
ways.extend(left)
if len(ways) == final_res_count:
    print(*ways)
else:
    print(-1)