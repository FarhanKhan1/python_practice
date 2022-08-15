
class stack:
    def __init__(self):
        self.stack=[]

    def push (self,a):
        if self.is_full():
            print("Stack is full")

        else:
            self.stack.append(a)

    def pop (self):
        if self.is_empty():
            print("stack is empty")

        else:
            self.stack.pop()

    def is_full(self):
        return len(self.stack)==2

    def is_empty(self):
        return len(self.stack)==0


stack_obj= stack()

stack_obj.push(12)
stack_obj.push(13)
stack_obj.push(14)
stack_obj.pop()
print(stack_obj.stack)

 