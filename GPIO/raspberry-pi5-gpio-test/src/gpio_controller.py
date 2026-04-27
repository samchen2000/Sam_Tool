class GPIOController:
    def __init__(self, gpio_pins, device_name):
        self.gpio_pins = gpio_pins
        self.device_name = device_name
        self.device_state = {pin: False for pin in gpio_pins}

    def setup_gpio(self):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        for pin in self.gpio_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def add_button(self, pin, callback):
        import RPi.GPIO as GPIO
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=callback, bouncetime=300)

    def toggle_device(self, pin):
        self.device_state[pin] = not self.device_state[pin]
        if self.device_state[pin]:
            print(f"{self.device_name} on GPIO {pin} is now ON")
        else:
            print(f"{self.device_name} on GPIO {pin} is now OFF")