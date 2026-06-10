# class Address:
#     def __init__(self,city,state):
#         self.city= city
#         self.state = state
        
#     def show(self):
#         print("the city is: ",self.city)
        
#     a = Address ("jaipur","rajasthan")
#     a.show()

# # inheritance

# class address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
    
#     def location(self):
#         return f"my location is {self.city}in{self.state}"
    
    
# class user:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def username(self):
#         print(f"my name is {self.name}")
        
# u = user ("tanmay",20)
# u.username()
# a = address("kukas","rajasthan")
# a.location()

# #encapsulation

# class address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
#     def location(self):
#         print(f"my location is {self.city} in {self.state} ")
        
# a = address("jaipur","rajasthan")
# a.location()
# print(a.city)
# print(a.state)

# #polymorphism

# class address:
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
#     def location (self):
#         print(f"my location is {self.city} in {self.state}")
        
# class hometown:
#     def __init__(self,city,state):
#         self.city =city
#         self.state = state
        
#     def location(self):
#         print(f"my home town location is {self.city} in {self.state}")
        
# a = address("vadodara","gujrat")
# a.location()
# b = hometown("jaipur","rajasthan")
# b.location()

# #class variable           not working

# class withdraw:
#     total = 0
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
#         withdraw.total +=1
        
#     def location(self):
#         print("location")
        
# a =withdraw("jaipur","rajasthan")

# b = withdraw("alwar","rajasthan")

# a.total
        
#overloading

def address(city,state):
    print(f"my address is {city} in {state}")
    
def address(city,state,country):
    print(f"my address is {city} at {state} in {country}")
    
address("jaipur","rajasthan")
address("jaipur","rajasthan","india")
