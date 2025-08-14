class newNode:
    def __init__(self, data):
        self.key = data
        self.parent = None
        self.count = 1
        self.left = None
        self.right = None


def insert(node, key, parent=None):
    if node == None:
        k = newNode(key)
        
        k.parent = parent
        if not k.parent:
            pass
        else:
            print(k.parent.key, end=" ")
        return k

    if key == node.key:
        (node.count) += 1
        print(node.key, end=" ")
        return node

    if key < node.key:
        node.left = insert(node.left, key, parent=node)
    else:
        node.right = insert(node.right, key, parent=node)
    return node

def lca(root, n1, n2, elements):
    if root is None:
        return None
    
    if(root.key > elements[n1] and root.key > elements[n2]):
        return lca(root.left, n1, n2, elements)
 
    if(root.key < elements[n1] and root.key < elements[n2]):
        return lca(root.right, n1, n2, elements)
 
    return root.key

n = int(input())
elements = list(map(int, input().split()))
ind1, ind2 = map(int, input().split())

mamad = {key:val for key,val in enumerate(elements)}

bst = None
for elem in elements:
    bst = insert(bst, elem)

res = lca(bst,ind1 - 1, ind2 - 1, elements)
for key, val in mamad.items():
    if val == res:
        print("\n",key+1,sep="")
        break