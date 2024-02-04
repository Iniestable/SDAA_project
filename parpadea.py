import pandas as pd
from sense_hat import SenseHat
from time import sleep
import keyboard

def Add(objeto, cantidad, data):      #Funcion para añadir objetos 
    counter = 0
    add = True
    salir = False
    for lee in data.values:         #Comprobacion de que es un objeto nuevo
        if lee[0] == objeto:
            print("El objeto ya esta en el almacen")
            salir = True
    if salir == False:
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


def Take(objeto, cantidad, data):      #Funcion para coger objetos
    counter = 0
    take = True
    found = False
    for lee in data.values:
        if lee[0] == objeto:
            found = True
            lee[1] = lee[1] - cantidad
            data.iloc[counter] = [lee[0], lee[1], lee[2]]       #Parte para editar los DF
            if lee[1] <= 0:
                print("Objeto gastado, liberando espacio")
                data = data.drop(data.index[counter]) 
                steve_pixels[lee[2]] = G                #Lo pinto en verde
            print(data)
            break     
        counter = counter + 1
    if found == False:
        print("El objecto no está en el almacen, no se puede sacar nada")
    return data

def parpadea(objeto, data):
    for lee in data.values:
        if lee[0] == objeto:        #Si encuentra el objeto
            if apagar == True:
                steve_pixels[lee[2]] = A
                apagar = False
            else:
                steve_pixels[lee[2]] = R        #Voy apagando y encendiendo el objeto
                apagar = True
            sleep(0.5)
              


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

sense = SenseHat()
data = pd.read_csv('datos_reservas.csv', header=0) #Leo datos y actualizo

    
while(1):
    for i in data.values:       #Recorro todos las posiciones de objetos de la lista
        steve_pixels[i[2]] = R 

    sense.set_pixels(steve_pixels)  #Pinto el mapa

    a = input("Dame un objeto: ")
    if a == "salir":
        break
    b = int(input("Dame un cantidad: "))
    c = input("Dame un c o m: ")

    if c == "c":
        data = Take(a, b, data)
    elif c == "m":
        data = Add(a, b, data)
    else: 
        print("Dato incorreto")
        while(True):
            parpadea(a, data)
            if keyboard.is_pressed("q"):
                print("q pressed, ending loop")
                break
        
