class vehicle:
   _year=1000 #notation for protected modifier
   __price=10000 #denote private variable

class tatamotors(vehicle):
    car_name="harrier"

t1 = tatamotors()
v1= vehicle() 
print(t1._year)   
# print(dir(v1)) 
print(v1._vehicle__price)  #the name of __price changes tp _vehicle__price where vehicle
#is th class name and this is called mandling  
print(t1._vehicle__price)

