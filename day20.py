# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1,2,3,4])
# y1 = [10,20,20,40]
# y2 = [20,30,25,30]
# w = .40
# plt.bar (x - w/2,y1,label="boys",width=w)
# plt.bar (x + w/2,y2,label="girls",width=w)
# plt.xlabel("groups")
# plt.ylabel("number of students")
# plt.title("number of students in each group")
# plt.legend()
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([1,2,3,4])
# y1 = [10,20,20,40]
# y2 = [20,30,25,30]
# y3 = [30,40,50,60]
# w = 1.00
# plt.bar (x - .33,y1,label="boys",width=w/3)
# plt.bar (x + .33,y2,label="girls",width=w/3)
# plt.bar (x,y2,label = 'teacher',width= w/3 )
# plt.xlabel("groups")
# plt.ylabel("number of students")
# plt.title("number of students in each group")
# plt.legend()
# plt.show()


# #histogram
# import matplotlib.pyplot as plt
# marks = [40,50,30,22,55,34]
# plt.hist(marks ,bins = 2)
# plt.show()

#pie chart
# import matplotlib.pyplot as plt
# fruits = ['apple','banana','mango','orange']
# count = [20,40,33,50]
# plt.pie(count, labels=fruits)

# plt.show()

# #pie chart percentage
# import matplotlib.pyplot as plt
# fruits = ['apple','banana','mango','orange']
# count = [20,40,33,50]
# plt.pie(count, labels=fruits,startangle=90,autopct="%1.1f%%")

# plt.show()

import matplotlib.pyplot as plt

#subplot
#first chart
x = [1,2,3,5,4]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.subplot(1,2,1)

plt.show()


