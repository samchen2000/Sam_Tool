from picamera2 import Picamera2, Preview
from time import sleep
from libcamera import Transform

picam2 = Picamera2()
picam2.preview_configuration.sensor.output_size = (2592, 1944)
#picam2.preview_configuration.sensor.output_exposure = 10000
#picam2.preview_configuration.sensor.output_gain = 1.0

picam2.start_preview(Preview.QTGL, transform=Transform(hflip=False, vflip=False))
picam2.start()
sleep(10)
picam2.close() 