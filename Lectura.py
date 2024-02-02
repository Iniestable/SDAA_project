from sense_hat import SenseHat

sense = SenseHat()

humidity = round(sense.get_humidity(), 2)
humedad = str(humidity) + "% de humedad"
print(humedad)
temp = round(sense.get_temperature(), 2)    #Para redondear a dos cifras la lectura
print(str(temp) + "ºC")