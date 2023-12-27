import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt
# Carga la imagen

imagen = cv2.imread('prueba.jpg')
img = cv2.cvtColor(imagen , cv2.COLOR_BGR2RGB) #Busca usar RGB
plt.imshow(img)
plt.title('aca')
plt.show()
# Obtiene las dimensiones y
# Vectoriza la imagen
a,l,c=tuple(img.shape)
pix=np.reshape(img,(a*l,c))
#Modelo de clustering
model=KMeans(5,random_state=42).fit(img)
palette=np.uint8(model.cluster_centers_)
plt.imshow([palette])
plt.show()