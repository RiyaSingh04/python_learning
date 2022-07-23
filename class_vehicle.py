# 22 july
class vehicle:
    def __init__(self,brand,color):
        self.brand = brand 
        self.color = color 

    def get_brand(self):
        return f'This brand is {self.brand}'            

class car (vehicle):
    def __init__(self,brand,color,type):
        super().__init__(brand,color)
        self.type = type
        self.brand = brand
    def get_color(self):
        return f'This color is {self.color}' 

    
    def get_type(self):
        return f'This type is {self.type}'


sedan = car('Toyota', 'Red', 'Sedan')
print(sedan.get_brand())
print(sedan.get_color())
print(sedan.get_type())                     