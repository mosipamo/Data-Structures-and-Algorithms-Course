import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        def __init__(self, val):
            self.val = val    
        

    def __init__(self):
        self.heap = []
        self.count = 0

    def bubble_up(self, index):
        if not isinstance(index, int):
            raise Exception(INVALID_INDEX)
        if not self.count:
            raise(EMPTY)
        if index < 0 or index >= self.count:
            raise Exception(OUT_OF_RANGE_INDEX)
        
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].val < self.heap[parent_index].val:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break


    def bubble_down(self, index):
        if not isinstance(index,int):
            raise Exception(INVALID_INDEX)
        if self.count <= 0:
            raise Exception(EMPTY)
        if index < 0 or index >= self.count:
            raise Exception(OUT_OF_RANGE_INDEX)
        
        while True:
            min_child_index = self.find_min_child(index)

            if min_child_index is None:
                break

            if self.heap[index].val > self.heap[min_child_index].val:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

    def heap_push(self, value):
        new_node = self.Node(value)
        self.heap.append(new_node)
        self.count += 1
        ind = self.count - 1
        self.bubble_up(ind)
        

    def heap_pop(self):
        if self.count <= 0:
            raise Exception(EMPTY)
        first_val = self.heap[0].val
        self.heap[0].val = self.heap[self.count - 1].val
        self.count -= 1
        self.heap.pop()
        if self.count:
            self.bubble_down(0)
        return first_val
        

    def find_min_child(self, index):
        if not isinstance(index,int):
            raise Exception(INVALID_INDEX)
        if index < 0 or index >= self.count:
            raise Exception(OUT_OF_RANGE_INDEX)
        if not self.count:
            raise Exception(EMPTY)
        
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index >= self.count:
            return None
        elif right_child_index >= self.count:
            return left_child_index
        else:
            return left_child_index if self.heap[left_child_index].val < self.heap[right_child_index].val else right_child_index

    def heapify(self, *args):
        for val in args:
            self.heap_push(val)

import heapq

class HuffmanTree:
    class Node:
        def __init__(self, letter, frequency, left=None, right=None):
            self.letter = letter
            self.frequency = frequency
            self.right = right
            self.left = left

        def __lt__(self, other):
            return self.frequency < other.frequency

    def __init__(self):
        self.letters = []
        self.freqs = []
        self.head = None

    def set_letters(self, *args):
        self.letters = list(args)

    def set_repetitions(self, *args):
        self.freqs = list(args)

    def build_huffman_tree(self):
        nodes = [self.Node(letter, frequency) for letter, frequency in zip(self.letters, self.freqs)]
        heapq.heapify(nodes)

        while len(nodes) > 1:
            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)
            new_node = self.Node(None, left.frequency + right.frequency, left, right)
            heapq.heappush(nodes, new_node)

        self.head = nodes[0]

    def get_huffman_code_cost(self):
        if not self.head:
            return 0
        def dfs(node, depth=0):
            if node:
                if not node.left and not node.right:
                    return depth * node.frequency
                return dfs(node.left, depth + 1) + dfs(node.right, depth + 1)
            return 0    
        return dfs(self.head)

    def text_encoding(self, text):
        let = {}
        for i in text:
            let[i] = let[i]+1 if i in let else 1
        self.letters= list(let.keys())
        self.freqs = list(let.values())
        self.build_huffman_tree()

class Bst:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return self.Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        for val in result:
            print(val, end=" ")

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
