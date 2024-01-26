import cv2
import numpy as np
from PIL import ImageGrab
from screeninfo import get_monitors
from ultralytics import YOLO

# Load the YOLOv8 models
model = YOLO('../models/GRS_V6s.pt')

monitor = get_monitors()[0]

# Loop through the video frames
while True:
    frame = np.array(ImageGrab.grab(bbox=(monitor.width/2, 0, monitor.width, monitor.height)))

    # Convert RGB color to BGR
    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Run YOLOv8 inference on the frame
    results = model(frame_bgr)

    # Visualize the results on the frame
    annotated_frame = results[0].plot(conf=True, labels=True, boxes=True, masks=True)

    # Detected boxes object
    boxes = results[0].boxes

    # Detected object classification
    probs = results[0].probs

    # Display the annotated frame
    cv2.imshow("YOLOv8 Inference", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close the display window
cv2.destroyAllWindows()