class ListQueue:
    def __init__(self):
        self.items = []
        self.front = self.rear = 0
        self.size = 3

    def enqueue(self,data):
        if self.size == self.rear:
            print("\n Queue is Full")

        else:
            self.items.append(data)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("\n Queue is empty")
        else:
            self.rear -= 1
            return self.items.pop(0)

# q = ListQueue()
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# print(q.items)
# print(q.dequeue())

# Limitation of list based is , it has a limited size

class Node():
    def __init__(self,data = None,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev
class NodeQueue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self,data):
        new_node = Node(data=data,next=None,prev=None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head

        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self):
        current = self.head
        if self.count==0:
            print("Queue is empty")
        elif self.count>1:

            data = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
            return data
        elif self.count == 1:
            self.count -= 1
            data = self.head.data
            self.head = None
            self.tail = None

            return data


q = NodeQueue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.dequeue())

cur = q.head
print(cur)
while cur:

    print(cur.data)
    cur = cur.next
