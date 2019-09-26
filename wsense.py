from sense_hat import SenseHat
import time
from datetime import datetime
from gpiozero import CPUTemperature


sense = SenseHat()

sense.set_rotation(180)

while True:
    cpu = CPUTemperature().temperature
    thermo = sense.get_temperature()
    temp = thermo-((cpu-thermo)/3)
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    if (cpu>70):
        sense.show_message("CPU TEMPERATURE CRITICAL %cpu C" % temp, scroll_speed=0.06, text_colour=[255, 0, 0])        
    sense.show_message("%.0f C" % temp, scroll_speed=0.06, text_colour=[100, 0, 0])
    sense.show_message("%.0f %%rH" % humidity, scroll_speed=0.06, text_colour=[10, 10, 100])
    sense.show_message("%.1f hPa" % pressure, scroll_speed=0.06, text_colour=[0, 100, 0])
    sense.show_message(datetime.now().strftime('%d/%m %H:%M'), scroll_speed=0.06, text_colour= [100,100,100])