class A:
    def __init__(self, a, **kwargs):        
        print("This is class A")
        self.a = a
        super().__init__(**kwargs)

    def get(self):
        print("This is A class")    

class B:
    def __init__(self, b, **kwargs):        
        print("This is class B")
        self.b = b
        super().__init__(**kwargs)

    def get(self):
        print("Tclashis B s")

class D:
    def __init__(self, d, **kwargs):
        self.d = d        
        print("This is class D")
        super().__init__(**kwargs)

class C(B, A, D):
    def __init__(self,first,second,third,fourth): #(c, **kwargs)
        print("This is class C")    
        self.c = third
        # super().__init__(a = first, b = second, d = fourth) # (*kwargs)
        # super(B, self).__init__()
        # super(A, self).__init__()

c_obj = C(1,2,3,4)
# print(c_obj.a, c_obj.b, c_obj.c, c_obj.d)
# print(help(c_obj))
print(help(c_obj))
# c_obj.get()
