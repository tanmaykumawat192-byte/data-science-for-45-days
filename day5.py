#nested list
list = [10,20,30,["hello","hello1","hello2",[True,False]]]
# print(list[0])
# print(list[1])
# print(list[2])

# print(list[3][0])
# print(list[3][1])
# print(list[3][2])

# print(list[3][3][0])
# print(list[3][3][1])

# for i in list:
#     if type(i) == list:
#         for j in i:
#             if type(j)==list:
#                 for k in j:
#                     print(k)
#                 else:
#                     print(j)
#             else:
#                  print(i)
            
# #function
# my_list = [10,20,30]
# def  square(x):
#     return x*x

# #map (2arguments)
# l = [10,20,30]
# l1 = list(map(square,l))
# print(l1)

#filter
def hello(x):
    return x.endwith('a')

l = ["apple","banana","cat","dog"]
l1 = list (filter(hello,l))
print(l1)
#example | alternative of filter
l1 = []
for i in l:
    if 'a'== i[-1]:
        l1.append(i)
        print(l1)
        
        
#nested dictionary
# d = {"age":20,"name":"hello"}
# d.update({"name":"arya mains"})
# d['name'] = "arya mains new"
# print(d)
# del (d['name'])

# l = [20,10]
# print(l[0])

# d = {"address":{"address1":{"city":"kukas city","district":"jaipur"},
#                 "address2":{"city":"gopalpura","district":"arya mains"}}}
# print(d["address"]["address1"]["city"])
# print(d["address"]["address1"]["district"])
# print(d["address"]["address2"]["city"])
# print(d["address"]["address2"]["district"])


# #try except
# try:
#     num1 = 10
#     num2 = 5
#     print (num1/num2)
# except:
#     print("hello except")
    
# #try except
# try:
#     num1 = 10
#     num2 = 0
#     print (num1/num2)
# except:
#     print("hello except")
    
# #try except and final

# try:
#     a =10
#     b = 5
#     print(a/b)
# except:
#     print("hello except")
# finally:
#     print("hello finally divide")