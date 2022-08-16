class queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,a):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue.insert(0,a)
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            self.queue.pop()
    def is_full(self):
        return len(self.queue) == 10
    def is_empty(self):
        return len(self.queue) == 0
obj_que = queue()
obj_que.enqueue(10)
obj_que.enqueue(12)
obj_que.enqueue(15)
obj_que.dequeue()
print(obj_que.queue)
