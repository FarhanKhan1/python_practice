#try and except
a = 1
b = 0
try:
    print(a/b)
except Exception as e:
    print("The error ",type(e), " Has been occured")
    print()
print("This is Pakistan")