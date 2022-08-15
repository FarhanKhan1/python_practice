# stack = []
# def push_(a):
#     if is_full():
#         print("Stack is full")
#     else:
#         stack.append(a)
#         print(stack)

# def pop_():
#     if is_empty():
#         print("Stack is empty")
#     else:
#         print(stack.pop())
#         print(stack)

# def is_empty():
#     return len(stack)==0

# def is_full():
#     return len(stack)==10

# while True:
#     choice = int(input("Enter 1: push(), 2:pop()"))

#     if choice == 1:
#         val = input("Enter a number to push: ")
#         push_(val)
    
#     elif choice == 2:
#         pop_()
    
#     else:
#         break








class Stack:
    def __init__(self):
        self.stack = []

    def push(self, a):
        if self.is_full():
            print("Stack is full")
        else:
            self.stack.append(a)

    def pop(self):
        if self.is_empty():
            print("Stack is Empty, Push some elements first")
        else:
            print(self.stack.pop())

    def is_empty(self):  
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack)==10



stack_obj = Stack()
   
stack_obj.push(12)
stack_obj.push(13)
stack_obj.pop()
print(stack_obj.stack)


































