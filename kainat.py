from re import U
class queue:
    def __init__(self):
         self.qu = []
    def enque(self):
        b = int(input("ENTER THE ELEMENT"))
        self.qu.insert(0,b)
    def deque(self):
        return self.qu.pop()
    def empty(self):
        return True if len(self.qu)==0 else False
    def full(self):
         return True if len(self.qu)==5 else False
queue_obj= queue()
queue_obj.enque()
queue_obj.enque()
queue_obj.enque()
queue_obj.deque()
print(queue_obj.qu)
