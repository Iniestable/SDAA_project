
Dic1 = ["Agua", 12, 0]
Dic2 = ["Culo", 23, 1]
lista = [Dic1, Dic2]
apagar = False
add = False
a = "Cola"
List_1 = []

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

for j in lista:
    steve_pixels[j[2]] = R  #Bucle para poner todos los objetos en rojo

for j in lista:
        if j[0] == a:       #Compruebo que el objeto este en la lista
            if apagar == True:
                steve_pixels[j[2]] = R
                apagar = False
            else:
                steve_pixels[j[2]] = A
                apagar = True
        else:
            add = True

if add == True:
    counter = 0
    for i in steve_pixels:      #Recorro todos los valores
        if i[0] == 0 and i[1] != 0 and add == True:     #Si hay un verde
            steve_pixels[counter] = R   #Lo pongo en rojo
            List_1 = [a, 50, counter]
            lista.append(List_1)
            print(lista)
            add = False
            break
        counter = counter + 1