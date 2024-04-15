import numpy as np
#Matplotlib tiene muchos modulos. Importar uno solo
import matplotlib.pyplot as plt


#Dibujar una funcion seno
#Crear ndarray de 1 dimension, 100 elementos equispaciados, de 0 a 2*PI


x=np.linspace(0,2*np.pi,100)
y=np.sin(x)

#Usar Matplotlib

plt.figure(figsize=(8,4))
plt.plot(x,y)
plt.show()
