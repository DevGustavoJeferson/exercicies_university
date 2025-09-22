import matplotlib.pyplot as plt
#from math import sqrt,log2,cos       #import math         #BIBLIOTECA DE FUNCOES MATEMATICAS
#x = math.sqrt(25)                    #x = math.sqrt(25)   #CALCULA A RAIZ QUADRADA


y = [1,2,3,4,5]
z = [2,4,1,3,5]

#plt.plot(y,z)
plt.bar(y,z)

plt.xlabel("EIXO X")
plt.ylabel("EIXO Y")

plt.box('Grafico de linha')

plt.show()
