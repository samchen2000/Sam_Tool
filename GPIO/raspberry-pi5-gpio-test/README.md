# Raspberry Pi 5 GPIO Test Software

This project is designed to control the hk4g4 device using the GPIO pins of the Raspberry Pi 5. Each GPIO pin is assigned a button that can toggle the state of the hk4g4 device.

## Project Structure

```
raspberry-pi5-gpio-test
├── src
│   ├── main.py          # Entry point of the application
│   ├── gpio_controller.py # Contains GPIOController class for GPIO management
│   └── config.py       # Configuration parameters for GPIO and hk4g4
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

## Installation

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd raspberry-pi5-gpio-test
   ```

2. **Install the required packages:**
   Make sure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Edit the `src/config.py` file to set up the GPIO pin mappings and any parameters related to the hk4g4 device.

## Running the Application

To start the GPIO test software, run the following command:
```
python src/main.py
```

## Usage

Press the buttons assigned to each GPIO pin to toggle the hk4g4 device on or off. The application will listen for button events and control the device accordingly.

## License

This project is licensed under the MIT License. See the LICENSE file for details.