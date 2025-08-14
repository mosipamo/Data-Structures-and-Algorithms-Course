import sys
import re


class Queue:
    def __init__(self):
        self.queue = []

    def getSize(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue) < 1:
            return True
        return False

    def getInOneLine(self):
        return ' '.join(self.queue)


class Stack:
    def __init__(self, size=10):
        self.stack = []
        self.size = size

    def isEmpty(self):
        if len(self.stack) < 1:
            return True
        return False

    def push(self, value):
        if len(self.stack) >= self.size:
            self.expand
        self.stack.append(value)

    def pop(self):
        if len(self.stack) < 0:
            return None
        return self.stack.pop()
        

    def put(self, value):
        if(len(self.stack) > 0):
            self.stack.pop()
        self.stack.append(value)

    def peek(self):
        if len(self.stack) < 1:
            return None
        return self.stack[len(self.stack) - 1]

    def expand(self):
        self.size *= 2

    def getInOneLine(self):
        return ' '.join(self.stack)

    def getSize(self):
        return len(self.stack)

    def getCapacity(self):
        return self.size


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getList(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.value)
            temp = temp.next
        return ' '.join(result)

    def insertFront(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        if temp == None:
            self.head = new_node
            return
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

    def reverse(self):
        if self.head == None:
            return
        
        p = self.head
        q = None
        r = None
        while p != None:
            r = q
            q = p
            p = p.next
            q.next = r
            
        self.head = q

class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
