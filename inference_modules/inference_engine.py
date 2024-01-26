import cv2
import numpy as np
from PIL import ImageGrab
from screeninfo import get_monitors
from ultralytics import YOLO
import threading

class InferenceEngine():
    def __init__(self, config, gui_model):
        print("Inference Engine Start")
        print(config)

        self.gui_model = gui_model

        self.model_path = "../models/" + config.get("model_name") + "/weights/" + config.get("model_name") + ".pt"
        self.proportion = config.get("proportion")
        self.input = config.get("input")
        self.preview = config.get("preview")

        self.model = YOLO(self.model_path)
        self.class_names = self.model.names
        self.monitor = get_monitors()[0]

        self.inference_thread = threading.Thread(target=self.inference_cycle)
        self.inference_status = False

    def start_inference(self):
        print("Inference Started")
        self.inference_status = True
        self.inference_thread.start()

    def stop_inference(self):
        print("Inference Stopped")
        self.inference_status = False

    def inference_cycle(self):
        monitor_width = 0
        if self.proportion.lower() == "full":
            monitor_width = 0
        elif self.proportion.lower() == "half":
            monitor_width = self.monitor.width / 2

        while self.inference_status:
            # Input Capture
            frame = np.array(ImageGrab.grab(bbox=(monitor_width, 0, self.monitor.width, self.monitor.height)))

            # Convert RGB color to BGR
            frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Run YOLOv8 inference on the frame
            results = self.model(frame_bgr)

            # Detected boxes object
            detected_classes = {}
            for i, result in enumerate(results):
                boxes = result.boxes
                for c in boxes.cls:
                    detected_classes[(self.class_names[int(c)])] = float(boxes.conf[i])

            if self.inference_status:
                self.gui_model.update_detected_classes(detected_classes)
                self.gui_model.update_inference_information(results[0].speed)

            if self.preview:
                # Visualize the results on the frame
                annotated_frame = results[0].plot()

                # Display the annotated frame
                self.gui_model.update_inference_preview_win(annotated_frame)