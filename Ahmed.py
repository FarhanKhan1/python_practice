"""
u1input = int(input("Enter length of the List: "))
list_1 = list()

#append

for i in range (1, u1input+1):
    list_1.append(i)
print ("List: ", list_1)
print (f'"List== "{list_1}')

#count

iinput = int(input("Enter number to count in the List: "))
counter = list_1.count (iinput)
print ("Number ", iinput, "is " ,counter, "times in the list")

#extend

list_2 = ['a','b']
print ("Second list: ", list_2)

list_2.extend(list_1)
print ("Extended second list is: ", list_2)

#index

print ("First List: ", list_1)
uindex1 = int(input("Enter the number you want to have index of: "))
index_1 = list_1.index(uindex1)
print ("index of ", uindex1, " is ",index_1 )

print ("Second List: ",list_2)
upop = int(input("Enter the number you want to pop: "))
pop1 = list_2.pop(upop)
print ("New List :", list_2)
"""

"""fruit=['Manago',' bnana']
fruit2=fruit.pop()
fruit.append("Price:50")
print(fruit)
print(fruit2)
print(type(fruit))
print(type(fruit2))
mylist=[1,2,3,4,5,6,7]
print """

car=["hnda","toyota","nissan"]
crr = car.pop(1)
print(crr)
