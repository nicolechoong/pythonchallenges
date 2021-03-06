import time, copy

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def __gt__(self, other):
        return self.cargo > other.cargo

class Queue:
    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.head is None:
            # If list is empty the new node goes first
            self.head = node
        else:
            # Find the last node in the list
            last = self.head
            while last.next:
                last = last.next
            # Append the new node
            last.next = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        return cargo

class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

class Golfer:
    def __init__(self, name, score):
        self.name = name
        self.score= score

    def __str__(self):
        return "{0:16}: {1}".format(self.name, self.score)

    def __gt__(self, other):
        return self.score < other.score    # Less is more

# 1. Write an implementation of the Queue ADT using a Python list. Compare the performance of this implementation to the ImprovedQueue for a range of queue lengths.

class QueueADT:
    def __init__(self):
        self.nodes = []

    def is_empty(self):
        return self.nodes == []

    def insert(self, cargo):
        self.nodes.append(cargo)

    def remove(self):
        self.nodes.pop()

t1 = time.time()
queue = Queue()
for i in range(0,10000):
    queue.insert(i)
t2 = time.time() - t1
print(t2)

t1 = time.time()
queue1 = QueueADT()
for i in range(0,10000):
    queue1.insert(i)
t2 = time.time() - t1
print(t2)

# Therefore QueueADT is more efficient

# 2. Write an implementation of the Priority Queue ADT using a linked list. You should keep the list sorted so that removal is a constant time operation. Compare the performance of this implementation with the Python list implementation.

class PriorityQueueADT:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        node = Node(item)
        self.items.append(node)
        self.items = sorted(self.items)

        for i in range(0,len(self.items)-1):
            self.items[i].next = self.items[i+1]
        self.items[-1].next = None

    def remove(self):
        print(self.items[-1])
        self.items.pop()

t1 = time.time()
queue2 = PriorityQueueADT()
for i in range(0,10000):
    queue2.insert(abs(10000-i))
t2 = time.time() - t1
print(t2)

print("\nNormal Queue Remove")
t1 = time.time()
for i in range(0,10000):
    queue1.remove()
t2 = time.time() - t1
print(t2)

print("\nPriority Queue Remove")
t1 = time.time()
for i in range(0,10000):
    queue2.remove()
t2 = time.time() - t1
print(t2)

# Performance is about the same
