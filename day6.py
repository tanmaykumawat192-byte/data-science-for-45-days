
# class tanmay:
#   def __init__(self,name):
#     self.name = name
#   def show(self):
#     print(self.name)
            
# t = tanmay("hello")
# t.show()


# class tanmay:
#     def __init__(self):
#      print("calling constructor")
       
#     def show():
#      print("show the name")
    
# t = tanmay()


# class tanmay:
#     def __init__(self,name,age):
#      self.name = name
#      self.age =age
     
#     def getAge(self):
#         print("my name is: ",self.age)
        
#     def getName(self):
#         print("my name is:",self.name)
         
# t = tanmay("hello",20)
# t.getAge()
# t.getName()

# class student:
#     def __init__(self,*args):
#       print(type(args))
#       print(args)
#       self.name = args[0]
      
#     def getStu(self):
#       print("the student is: ",self.name)

      
# s = student("hello",20,"00000000","arya@gmail.com")
# s.getStu()

# class student:
#     def __init__(self,args):
#         print(type(args))
#         print(args)
#         self.name = args
#     def getStu(self):
#         return self.name    


# s = student({"name":"hello","age":20})
# t= s.getStu()
# print(t["age"])

class student:
    def __init__(self,*args):
      self.data = args
      
    def users(self):
      for i in self.data[0]:
           print(i)
           
    def details(self):
      print(self.data[1])
      
      
      for i in self.data[1]:
            print()
            
            
s=student(["tanmay","nikhil","vishu","bilal","harsh"],{"address":"jaipur","college":"arya",})  
s.detail()