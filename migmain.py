#ХОЧУ ДОМОЙ
#не знаю что еще придумать и я устал
from matplotlib import pyplot as plt
#добавление обозначений
plt.title('Машинки')
plt.xlabel('Значение Х1')
plt.ylabel('Значение X2')
#делаем оси
plt.xlim(0,50)
plt.ylim(0,50)
plt.scatter(19, 13, c= 'orange')
plt.scatter(14, 17, c= 'blue')
#прямые добавлены
plt.plot
plt.plot([19, 19],[0, 20])
plt.plot([0,35.25],[28.2, 0])
#точки х у 2222
X = [0, 34/3]
Y = [40/5, 0]
#постоение прямой по точке
plt.plot(X, Y)
# #создание вектора

plt.text(1.2, 19.5, 'X2 <= 19',fontsize=10)
plt.text(25, 10, '4X1 + 5X2 <= 141',fontsize=10)
plt.text(6.5, 4, 'перпендикуляр',fontsize=10)
#display the graph
plt.show()
#слишком сложно 