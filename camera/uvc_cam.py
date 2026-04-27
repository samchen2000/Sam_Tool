import cv2

# Initialize the camera object (0 is usually the default USB camera)
cam = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cam.isOpened():
    print("Error: Could not open camera.")
else:
    # Read a frame from the camera
    ret, image = cam.read()

    if ret:
        # Save the image
        cv2.imwrite('/home/pi/testimage.jpg', image)
        print("Image captured and saved as testimage.jpg")
    else:
        print("Error: Failed to capture image.")

# Release the camera
cam.release()
