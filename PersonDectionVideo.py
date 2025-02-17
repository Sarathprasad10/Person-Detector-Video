import cv2
import datetime
import imutils
import numpy as np

protopath = r'C:\Users\LENOVO\Desktop\PersonDetection in Video\MobileNetSSD_deploy.prototxt'
modelpath = r'C:\Users\LENOVO\Desktop\PersonDetection in Video\MobileNetSSD_deploy.caffemodel'
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
           "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]


cap= cv2.VideoCapture(r'C:\Users\LENOVO\Desktop\PersonDetection in Video\Cristiano Ronaldo Walks Out For His Second Manchester United Debut At Old Trafford.mp4')


fps_start_time =datetime.datetime.now()
fps=0
total_frames =0
while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame,width=500)
    total_frames=total_frames+1


    (H,W)=frame.shape[:2]

    blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 127.5)
    print(f"Blob created: {blob.shape}")

    detector.setInput(blob)
    person_detections = detector.forward()

    for i in np.arange(0, person_detections.shape[2]):
        confidence = person_detections[0, 0, i, 2]
        print(f"Confidence for detection {i}: {confidence}")

        if confidence > 0.2:
            print(f"Detection {i} with confidence: {confidence}")
            idx = int(person_detections[0, 0, i, 1])
            if CLASSES[idx] != "person":
                continue

            person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = person_box.astype("int")
            print(f"Person detected at [{startX}, {startY}, {endX}, {endY}]")

            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 0, 255), 2)



    fps_end_time=datetime.datetime.now()
    time_diff =fps_end_time-fps_start_time
    if time_diff.seconds ==0:
        fps=0.0
    else:
        fps =(total_frames/time_diff.seconds)
    
    fps_text="FPS:{:.2f}".format(fps)
    
    cv2.putText(frame,fps_text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)

    cv2.imshow("Application",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release() 
cv2.destroyAllWindows() 