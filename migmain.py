from matplotlib import pyplot as plt
plt.title('Машинки')
plt.xlabel('Значение Х1')
plt.ylabel('Значение X2')
plt.xlim(0,50)
plt.ylim(0,50)
plt.scatter(19, 13, c= 'orange')
plt.scatter(14, 17, c= 'blue')
plt.plot([0,20],[17, 17])
plt.plot([19, 19],[0, 20])
plt.plot([0,35.25],[28.2, 0])
X = [0, 34/3]
Y = [40/5, 0]