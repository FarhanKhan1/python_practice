#encapsulation
#Abstraction
#Inheritence 

class Phone_class: #parent/base class
    def __init__(self, brand_name, launch_year, screen_size):
        self.brand_name = brand_name
        self.launch_year = launch_year
        self.screen_size = screen_size

    def get_name_launch(self):
        return f"name: {self.brand_name} and Launching year is: {self.launch_year} "

class Smartphone_class(Phone_class): #child/derived class 
    def __init__(self, cpu, ram, camera, brand, l_year, screen):
        super().__init__(brand, l_year, screen)
        self.cpu = cpu
        self.ram = ram
        self.camera = camera





# a = 100
# brand = input("Enter Brand name: ")
s_phone = Smartphone_class('8 GH', '4-GB', '12-MP', 'SAMSUNG', '2021', '8"')
print(s_phone.camera)
print(s_phone.get_name_launch())
print(s_phone.__dict__)
print(help(s_phone))
# 
# # s_phone1 = Smartphone_class('2 GH', '6-GB', '32-MP', 'Infinix', '2020', '7"')


        
        
