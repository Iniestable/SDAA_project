from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
Dic1 = ["Agua", 12, 2]
Dic2 = ["Culo", 23, 7]
lista = [Dic1, Dic2]
apagar = False

# Define some colours
R = (255, 0, 0)
G = (0, 255, 0)
W = (255, 255, 255)
A = (0, 0, 0)

# Set up where each colour will display
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

counter = 0

for j in lista:
    steve_pixels[j[2]] = R  #Bucle para poner todos los objetos en rojo


sense.set_pixels(steve_pixels)  #Primero se ponen en este color

while(1):
    for j in lista:
        if j[0] == "Agua":
            if apagar == True:
                steve_pixels[j[2]] = R
                apagar = False
            else:
                steve_pixels[j[2]] = A
                apagar = True
    
    sleep(1)
    sense.set_pixels(steve_pixels)  #Luego todos rojos

