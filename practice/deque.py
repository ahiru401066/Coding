class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def peekFront(self):
        if self.head is None: return None
        else: return self.head.data

    def peekBack(self):
        if self.tail is None: return None
        else: return self.tail.data

    def enqueueFront(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev


    def enqueueBack(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def dequeueFront(self):
        if self.head is None: return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return temp

    def dequeueBack(self):
        if self.tail is None: return None
        temp = self.tail
        self.tail = self.tail.prev
        if self.tail is None: self.head = None
        else: self.tail.next = None
        return temp.data
    

q = Deque()
print(q.enqueueBack(4))
print(q.enqueueBack(50))
print(q.peekFront())
print(q.peekBack())
print(q.enqueueFront(36))
print(q.enqueueFront(96))
print(q.peekFront())
print(q.peekBack())
print(q.dequeueBack())
print(q.dequeueBack())
print(q.peekFront())
print(q.enqueueFront(20))
print(q.dequeueBack())