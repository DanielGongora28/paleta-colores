from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt
from django.http import HttpResponse

# Create your views here.
def processing(request):
    imagen = np.array(cv2.imread(r'C:\Users\danie\OneDrive\Escritorio\djangoproject\modelokm\prueba.jpg'))
    #:Hacerle esto al resultad0-->img = cv2.cvtColor(imagen , cv2.COLOR_BGR2RGB) #Busca usar RGB
    # Obtiene las dimensiones y
    # Vectoriza la imagen
    a,l,c=tuple(imagen.shape)
    pix=np.reshape(imagen,(a*l,c))
    return pix#HttpResponse(pix)
