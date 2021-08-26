import random
import matplotlib.pyplot as plt

#Generar un numero aleatorio
print(random.randrange(10,100,2))

#Reacomodar una lista al azar
lista = [1,2,3,4,5,6,7,8,9,10]
print("Lista original", lista)

#Mezcla los elementos de la lista al azar
random.shuffle(lista)

#Imprime la lista mezclada
print("Lista mixeada", lista)

#Generea una grafica de campana de GAUSS
#Genera los datos de la grafica
campana = [random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)

plt.show()