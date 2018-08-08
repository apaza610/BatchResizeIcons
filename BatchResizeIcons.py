############################################
# Batch resize images for FreePlane mindmaps
#
############################################

from PIL import Image
import os

size = (24,24)        #tupla
os.makedirs('./salida')

list = os.listdir("./")
for elemento in list:
    if str(elemento).endswith('.png'):
        im = Image.open(elemento)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save('./salida/'+elemento)
