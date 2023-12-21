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

q = ListQueue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.items)
print(q.dequeue())

# Limitation of list based is , it has a limited size
