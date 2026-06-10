#Class methods and self

# class address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#     def show(self):
#         print("The city is: ", self.city)
# a = address("jaipur", "rajasthan")
# a.show()

# Inheritance

# class address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#     def location(self):
#         return f" the city is {self.city} in {self.state}"
# class user(address):
#     def __init__(self,name,age,city,state):
#         self.name = name 
#         self.age = age
#         # self.city = city 

#         # self.state = state
#         super().__init__(city, state)
#     def userName(self):
#         print (f"my name is {self.name}")
# u= user("harsh",20,"jaipur","rajasthan")
# u.userName()
# print(u.location())

# Encapsulation

# class address:
#     def __init__(self,city,state):
#         self.__city = city # private attribute
#         self.state = state
#     def location(self):
#         print(f"the city is {self.__city} in {self.state}")
#     def get_city(self):
#         return self.__city
# a = address("chhapra", "bihar")
# a.location()
# print (a.__city) 
# print(a.get_city())
# print(a.state)

#Polymorphism

# class address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#     def location(self):
#         print (f" the city is {self.city} in {self.state}")
# class homeTown(address):
#     def __init__(self,city,state):
#         self.city = city
#         self.state = state
#     def location(self):
#         print (f" the home town is {self.city} in {self.state}")
# a = address("vadora", "gujarat")
# a.location()
# b = homeTown("chhapra", "bihar")
# b.location()

#class variables
# class address:
#     total = 0 # class variable
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#         address.total += 1
#     def location(self):
#         print("location")
# a= address("jaipur", "rajasthan")

# b= address("chhapra", "bihar")
# a.location()
# print(address.total)

# overloading and overriding

# def address(city, state):
#     print(f"my address is {city} in {state}")

# def address(city, state, country):
#     print(f"my address is {city} at {state} in {country}")
# # address("jaipur", "rajasthan") # Error show because the second function is overriding the first function and we cannot have two functions with same name in python.
# address("jaipur", "rajasthan", "india")
 
# class address:
#     def __init__(self, city, state):
#         self.city = city
#         self.state = state
#     def location(self):
#         print("location")
# class user(address):
#     def __init__(self,name,age,city,state):
#         self.name = name 
#         self.age = age
#     def location(self):  #method overriding
#         print ("user location")
# u = user("arya mains",20,"jaipur","rajasthan")
# u.location()

# Tuples

# t = (10,20,30)
# print(t[0])
# print(t[-1])

# example
# marks = [98,90,80,95]

#list -> change
# marks[3] = 50
# print(type(marks))
# print(marks)

#tuple -> not change
# t = tuple(marks)
# print(type(t))
# print(t)

#tuple into list
# m = list(t)
# print(type(m))
# print(m)