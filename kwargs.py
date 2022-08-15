"""
*args
**kwargs

"""

def args(*args):
    print(type(args))


     
def kwargs(**kwargs):
    print(kwargs)     

def kwargs(a,**kwargs):
    print(kwargs)

# args(2,3,4,5,6)
# kwargs(12, a=2, b=3, c=4)
kwargs(a=2, b=3, c=4)