import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt
import streamlit as st
# Carga la imagen

def model(img,colorwave):
    if colorwave.is_integer():
        imagen = cv2.imread(colorwave)
        img = cv2.cvtColor(imagen , cv2.COLOR_BGR2RGB) #Busca usar RGB
        # Obtiene las dimensiones y Vectoriza la imagen
        a,l,c=tuple(img.shape)
        pix=np.reshape(img,(a*l,c))
        #Modelo de clustering
        model=KMeans(colorwave,random_state=42).fit(pix)
        palette=np.uint8(model.cluster_centers_)
        return imagen, palette
    else:
        return 'Use un numero de colores Valido 🚧'