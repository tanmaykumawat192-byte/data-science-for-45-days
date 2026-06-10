#dict
d = {'name' : ' hello','age':20}
print(d.keys())
print(d.values())

for i in d.keys():
    print("keys=",i)
    print("value=",d[i])
    
# # function

# def hello():
#     print("hello function is working")   
# hello()

# def hello(a):  #a as a parameter
#     print(a)
# hello (100) # 100 as a argument

# def add(a,b):
#     print(a+b)
# add(10,5)

# def student(*a):
#     print(a)
#     print (type(a))
    
# student(1,2,3,4,5,6)

# def marks (a):
#     for i in a:
#         print (i)
    
#     marks(10,20,30,40,50)
    
# def address(a):
#     for i in a:
#         for j in i:
#             print(j)
    
# address(["hello","tanmay"])



# #lambda function

# add = lambda x:x
# print(add(100))

# sum =lambda x,y: x+y
# print (sum(10,20))


# # list 

# list = [10,20,30]
# print(len(list))
# print(list[0])
# print(list[-1])
# print(list[-2])

# #append
# list.append(40)
# print(list)

# #insert
# list.insert(1,100)
# print(list)

# l = [10,20,30,{"name":"yourname","address":["jaipur","kukas","home toen","friend name"]}]
# print(l[3]['address'])
# print(l[3]['name'])
# for i in l[3]['name']:
#   for j in l[3]['address']:
#     print (i)
#     print (j)
    
