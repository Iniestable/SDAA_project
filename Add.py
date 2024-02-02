from sense_hat import SenseHat
from time import sleep
import pandas as pd

def Add(objeto, cantidad, data):      #Funcion para añadir objetos 
    counter = 0
    add = True
    for i in steve_pixels:      #Recorro todos los valores
        if i[0] == 0 and i[1] != 0 and add == True:     #Si hay un verde
            steve_pixels[counter] = R   #Lo pongo en rojo
            List_1 = [objeto,cantidad,counter]
            data = data.append(pd.Series(List_1, index=data.columns), ignore_index=True)
            print(data)
            add = False
        elif counter >= 55 and add == True:
            print("Almacenamiento completo")
            add = False
            
        counter = counter + 1

    return data


# Definicion de Variables
R = (255, 0, 0)
G = (0, 255, 0)
W = (255, 255, 255)
A = (0, 0, 0)


steve_pixels = [
    G, G, G, G, G, G, G, G,
    G, W, G, G, W, G, G, W,
    G, W, G, G, W, G, G, W,
    G, W, G, G, W, G, G, W,
    G, W, G, G, W, G, G, W,
    G, W, G, G, W, G, G, W,
    G, W, G, G, W, G, G, W,
    W, W, W, W, W, W, W, W
]


data = pd.read_csv('datos.csv') #Leo datos y actualizo

for i in data.values:       #Recorro todos las posiciones de objetos de la lista
    steve_pixels[i[2]] = R 

new_data = Add("Manzana", 150, data)
new_data.to_csv('datos.csv', index=False)
    
    
sense.set_pixels(steve_pixels)  #Pinto el mapa