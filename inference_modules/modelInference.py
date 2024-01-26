from ultralytics import YOLO

# Load a models
model = YOLO('../models/GRS_V6s.pt')  # pretrained YOLOv8n models

# Get Model Class Names
class_names = model.names

# Source
source = "screen"

# Run batched inference on a list of images
results = model(source, stream=True)  # return a generator of Results objects

# Process results generator
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    probs = result.probs  # Probs object for classification outputs

    for c in boxes.cls:
        print(class_names[int(c)])