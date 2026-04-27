from gpiozero import LED, Button
from time import sleep
from signal import pause

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

#button = Button(3)

#button.when_pressed = led.on
#button.when_released = led.off

led1.on()
led2.on()
led3.on()

sleep(2) 

led1.off()
led2.off()
led3.off()



pause()