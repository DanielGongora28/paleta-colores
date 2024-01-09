import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans
from functions import model

st.set_page_config(page_title = 'Get Color Palette', # Nombre de la página 
                   page_icon = '🎨', # Ícono de gráfico de barras de la página
                   layout = 'wide') # Utilizar la página completa en lugar de una columna central estrecha


page_bg_img="""<style>[data-testid="stAppViewContainer"]{background-color: #ffffff;
             background-image: url("https://wallpapertag.com/wallpaper/full/1/9/4/143491-backgrounds-images-2560x1600-windows-7.jpg");
             background-size: cover;
             }
             </style>
             """
        
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style = 'text-align: center;color:#03073d;font-size: 85px; font-family:Georgia; font-weight: bold;border: 3px solid #0d0a78;border-radius: 30px;box-shadow: 0px 0px 40px #03077d'>Lets get the color palette of your images 🎨 </h1>", unsafe_allow_html =True)



c1,sep,c2=st.columns([1.5,0.1,2])
c1.text("")
c1.text("")
c1.markdown("<h2 style= 'text-align: center;color:#03073d;font-size: 50px; font-family: Georgia; font-weight: normal;border: 3px double #0d0a78;border-radius: 30px;: 0px 0px 40px #03077d'> \n Load your image 💽</h2>",unsafe_allow_html=True)
img=c1.file_uploader(label="",type=['png','jpg'])
if not img:
    c1.text("")
else:
    c1.image(img)

c2.text("")
c2.text("")
if not img:
    c2.text("")
else:
    c2.text("")
    c2.markdown("<h3 style= 'text-align: center;color:#03073d;font-size: 30px; font-family: Georgia; font-weight: normal;border-bottom: 2px solid #03073d;'>How many colors do you want to get?</h3>", unsafe_allow_html=True)
    #c2.text("¿How many colors you wanna get? ")
    colors=c2.slider(label="",
              min_value=1,
              max_value=10,
              step=1
              )