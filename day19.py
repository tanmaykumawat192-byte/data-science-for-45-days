# #Create first chart
# import matplotlib.pyplot as plt
# x = [2010,2015,2020,2025]
# y = [100,200,250,300]  
# plt.plot(x,y)  #Line chart

# plt.xlabel("years")
# plt.ylabel("sales report")# 
# plt.title("sales report")
# plt.show()  #Show graph


# import matplotlib.pyplot as plt
# x = [2010,2015,2020,2025]
# y = [100,200,250,300] 
# #graph size
# plt.figure(figsize=(6,2))
# plt.plot(x,y , color="blue",marker = '*',linestyle = ":",linewidth=4,markersize=14)
# plt.show()

# #multi lines chart

# import matplotlib.pyplot as plt

# x = [2010,2015,2020,2025]

# y1 = [100,300,200,400]
# y2 = [200,100,300,500]
# plt.plot(x,y1,label= "Tshirt" )
# plt.plot(x,y2,label="paints")
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt

# x = [2000,2010,2020,2025]
# y1 = [50,150,130,300]
# y2 =[20,100,90,250]

# plt.plot(x,y1,label="flat sale")
# plt.plot(x,y2,label="House sale")
# plt.xlabel("years")
# plt.ylabel("sales report")
# plt.title("Flat and house sales report")
# plt.legend()
# plt.show()

# Bar chart
# import matplotlib.pyplot as plt
# x = [2015,2020,2025,2030]
# y = [100,200,230,300]
# #size
# plt.figure(figsize=(6,2))
# plt.bar(x,y)

# plt.show()

#multi bar chart
import matplotlib.pyplot as plt
x = [1,2,3,4]
y1 = [10,20,20,40]
y2 = [20,30,25,30]
w = .40
plt.bar (x - w/2,y1,label="boys",width=w)
plt.bar (x + w/2,y2,label="girls",width=w)
plt.bar (x,y1)
plt.bar(x,y2)
plt.show()