from ultralytics import YOLO

# Load a model
model = YOLO("helmet.pt")  # load a pretrained model (recommended for training)

# Use the model
results = model("helmet.mp4")  # predict on an image