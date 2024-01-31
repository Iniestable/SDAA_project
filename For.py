from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
Dic1 = ["Agua", 12, 2]
Dic2 = ["Culo", 23, 7]

# Define some colours
R = (255, 0, 0)
G = (0, 255, 0)
W = (255, 255, 255)

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

steve_pixels[Dic1[2]] = R
steve_pixels[Dic2[2]] = R

sense.set_pixels(steve_pixels)  #Primero se ponen en este color

for i in steve_pixels:
  if i[0] == 0 and i[1] != 0:
    steve_pixels[counter] = R
  counter = counter + 1
  
sleep(1)
sense.set_pixels(steve_pixels)  #Luego todos rojos

