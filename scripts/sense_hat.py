# documentation: https://sense-hat.readthedocs.io/en/latest/

from sense_hat import SenseHat
import time

sense = SenseHat()

# orientation = sense.get_orientation_degrees()
# print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

# while 1:
#     sense.show_message("Jim", text_colour=[255, 0, 0],back_colour=[255, 255, 0])
sense.clear()

while 1:
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    humidity = sense.get_humidity()
    print("Humidity: %s %%rH" % humidity)
    pressure = sense.get_pressure()
    print("Pressure: %s Millibars" % pressure)

    temp = sense.get_temperature_from_humidity()
    print("Temperature: %s C(from humidity sensor)" % temp)
    temp = sense.get_temperature_from_pressure()
    print("Temperature: %s C(from pressure sensor)" % temp)
    print()
    time.sleep(10)