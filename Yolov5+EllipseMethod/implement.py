import torch
import cv2
# loads a video file and returns bounding box detections
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt',force_reload=True)
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1 # maximum number of detections per image
model.amp = False  # Automatic Mixed Precision (AMP) inference

img = cv2.VideoCapture("Test.mp4") #Change the path to your video file
while(img.isOpened()):
    ret, frame = img.read() # read a frame
    results = model(frame)  # inference
    for box in results.xyxy[0]:   # box is a list of 4 numbers
        if box[5]==0:       # if the confidence is 0, then skip       
            xB = int(box[2])   # xB is the x coordinate of the bottom right corner
            xA = int(box[0])   # xA is the x coordinate of the top left corner
            yB = int(box[3])   # yB is the y coordinate of the bottom right corner
            yA = int(box[1])   # yA is the y coordinate of the top left corner
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2) # draw a rectangle around the detected object
            cv2.circle(frame, (int((xA+xB)/2), int((yA+yB)/2)), 2, (0, 0, 255), -1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break