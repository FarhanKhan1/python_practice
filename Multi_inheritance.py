"""class A:
    def __init__(self):
        print("This is called A")

class B:
    def __init__(self):
        print("This is called B")

class D:
    def __init__(self):
        print("This is called D")
    
class C(A,B,D):
    def __init__(self):
        super().__init__()
        D.__init__(self)
        B.__init__(self)
        print ("This is class C")

c_obj=C() 
"""

class A:
    def __init__(self):
        self.A=A

class B(A):
    def __init__(self):
        super().__init__()
        self.B=B

class D(B):
    def __init__(self,a,b,d):
        super().__init__()
        B.__init__(self)
        self.D=D


a,b,d = 3,6,8
D_obj= D(a,b,d)
print(D_obj.__dict__)