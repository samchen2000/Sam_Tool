"""headless test for mipi_camera_gui image adjustments

This script captures one frame from camera index 0 (or a video file if provided
via env var TEST_VIDEO), applies the same basic adjustments (RGB multipliers,
contrast, brightness, hue shift, saturation multiplier) and writes snapshot.
"""
import os
import time
import cv2
import numpy as np

# parameters (choose some non-defaults to exercise code)
params = {
    'brightness': 10.0,
    'contrast': 1.1,
    'saturation': 1.2,
    'hue': 15.0,
    'r_mul': 1.0,
    'g_mul': 0.9,
    'b_mul': 1.1,
}

video_src = os.environ.get('TEST_VIDEO', '0')
cap = None
try:
    cam_index = int(video_src)
    cap = cv2.VideoCapture(cam_index, cv2.CAP_V4L2)
    if not cap.isOpened():
        cap.release()
        cap = cv2.VideoCapture(cam_index)
except Exception:
    try:
        cap = cv2.VideoCapture(video_src)
    except Exception:
        cap = None

if cap is None or not cap.isOpened():
    print('無法開啟相機或影片來源，使用合成測試影像')
    # create synthetic test image (gradient + color bars)
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    for y in range(frame.shape[0]):
        frame[y, :, :] = (y * 255 // frame.shape[0])
    bar_w = frame.shape[1] // 6
    colors = [ (0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,255), (255,255,0) ]
    for i,c in enumerate(colors):
        x0 = i*bar_w
        x1 = x0 + bar_w
        frame[:, x0:x1, 0] = c[0]
        frame[:, x0:x1, 1] = c[1]
        frame[:, x0:x1, 2] = c[2]
    got_frame = True
else:
    got_frame = False

if not got_frame:
    # read a few frames to let camera auto-adjust
    for _ in range(5):
        ret, frame = cap.read()
        if not ret:
            break
        time.sleep(0.05)

    ret, frame = cap.read()
    if not ret:
        print('無法取得影格，改用合成影像')
        # create synthetic fallback image
        frame = np.zeros((480, 640, 3), dtype=np.uint8)
        for y in range(frame.shape[0]):
            frame[y, :, :] = (y * 255 // frame.shape[0])
        bar_w = frame.shape[1] // 6
        colors = [ (0,0,255), (0,255,0), (255,0,0), (0,255,255), (255,0,255), (255,255,0) ]
        for i,c in enumerate(colors):
            x0 = i*bar_w
            x1 = x0 + bar_w
            frame[:, x0:x1, 0] = c[0]
            frame[:, x0:x1, 1] = c[1]
            frame[:, x0:x1, 2] = c[2]
        got_frame = True

frame = cv2.resize(frame, (640, 480))
img = frame.astype(np.float32)
# apply RGB multipliers (BGR order)
img[...,0] *= params['b_mul']
img[...,1] *= params['g_mul']
img[...,2] *= params['r_mul']
# contrast/brightness
img = img * params['contrast'] + params['brightness']
img = np.clip(img, 0, 255).astype(np.uint8)
# HSV adjust
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
hue_shift = params['hue']
sat_mul = params['saturation']
hsv[...,0] = (hsv[...,0] + (hue_shift * 179.0 / 360.0)) % 180.0
hsv[...,1] = np.clip(hsv[...,1] * sat_mul, 0, 255)
img2 = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

outname = f'headless_snapshot_{int(time.time())}.png'
cv2.imwrite(outname, img2)
print('Saved', outname)
cap.release()
