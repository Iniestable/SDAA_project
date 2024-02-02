from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
print(humidity)
temp = sense.get_temperature()
print(temp)