# print("THIS IS INHERETENCE")
class A:
    def __init__(self, a):
        self.a = a

    def get_info(self):
        print(f" This is A: {self.a}")

class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b
    
    def get_info(self):
        print(f" This is B: {self.b}")

class C(B):
    def __init__(self, a,b,c):
        B.__init__(self,a,b)
        self.c = c

    # def get_info(self):
    #     print(f" This is C class: {self.c}")    

a, b, c = 2,4,6
obj = C(a,b,c)
# print(dir(obj))
# print(help(obj))
# print(obj.a, obj.b, obj.c)
# print(obj.__dict__)
obj.get_info()

