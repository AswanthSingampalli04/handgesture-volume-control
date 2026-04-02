# Installing required libraries (run these commands in terminal first):
# pip install mediapipe
# pip install opencv-python mediapipe pycaw comtypes numpy


import cv2
import numpy as np
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize MediaPipe Hand model
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Create hand landmarker
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
hand_landmarker = vision.HandLandmarker.create_from_options(options)

# Get system audio interface
devices = AudioUtilities.GetSpeakers()
volume = devices.EndpointVolume

# Get volume range
vol_min, vol_max = volume.GetVolumeRange()[:2]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for natural interaction
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert to RGB and create MediaPipe image
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=img_rgb)
    results = hand_landmarker.detect(mp_image)

    if results.hand_landmarks:
        hand_landmarks = results.hand_landmarks[0]

        # Get coordinates of thumb tip (landmark 4) and index finger tip (landmark 8)
        thumb_tip = hand_landmarks[4]
        index_tip = hand_landmarks[8]

        # Convert normalized coordinates to pixel values
        x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
        x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

        # Draw circles on thumb and index finger tips
        cv2.circle(frame, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # Calculate distance between thumb and index finger
        length = np.hypot(x2 - x1, y2 - y1)

        # Map the length to volume range
        # You may need to adjust min and max length values based on your setup
        vol = np.interp(length, [30, 200], [vol_min, vol_max])
        volume.SetMasterVolumeLevel(vol, None)

        # Display volume bar
        vol_bar = np.interp(length, [30, 200], [400, 150])
        cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(frame, (50, int(vol_bar)), (85, 400), (0, 255, 0), cv2.FILLED)

        # Display volume percentage
        vol_perc = np.interp(length, [30, 200], [0, 100])
        cv2.putText(frame, f'{int(vol_perc)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                    1, (0, 255, 0), 3)

    cv2.imshow("Volume Control", frame)

    # Enhanced key handling for application control
    key = cv2.waitKey(1) & 0xFF
    
    # Multiple exit keys for user convenience
    if key == 27 or key == ord('q') or key == ord('Q') or key == ord('x') or key == ord('X'):
        print("Application stopped by user key press")
        break
    
    # Display instructions when help is requested
    if key == ord('h') or key == ord('H'):
        cv2.putText(frame, "Press ESC, Q, or X to exit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, "Press H for help", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow("Volume Control", frame)
        cv2.waitKey(2000)  # Show help for 2 seconds

cap.release()
cv2.destroyAllWindows()
