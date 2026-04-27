# main.py

import RPi.GPIO as GPIO
import time
from gpio_controller import GPIOController
from config import GPIO_CONFIG

def main():
    # Initialize GPIO settings
    GPIO.setmode(GPIO.BCM)
    gpio_controller = GPIOController()

    # Setup GPIO pins
    gpio_controller.setup_gpio(GPIO_CONFIG)

    try:
        # Main loop to listen for button events
        while True:
            time.sleep(0.1)  # Prevent CPU overload
    except KeyboardInterrupt:
        print("Exiting program.")
    finally:
        GPIO.cleanup()  # Clean up GPIO settings

if __name__ == "__main__":
    main()