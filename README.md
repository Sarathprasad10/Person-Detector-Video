﻿# Person-Detector-Video

### Purpose
The goal of this project is to process a video stream, detect persons using a pre-trained MobileNet SSD model, and display bounding boxes around the detected persons in real-time. The MobileNet SSD model is capable of detecting multiple object classes, including persons, cars, and bicycles. This project demonstrates how to use a deep learning model to detect objects in video frames efficiently.

### Libraries and Files
- **OpenCV (`cv2`)**: OpenCV is used for video capture, image processing, and drawing bounding boxes around detected persons.
- **NumPy**: NumPy is used for array manipulation, particularly in scaling and processing bounding box coordinates.
- **imutils**: A utility library used for resizing video frames to a suitable size for processing.
- **MobileNetSSD Model Files**:
  - **Prototxt (`MobileNetSSD_deploy.prototxt`)**: Defines the architecture of the MobileNet SSD model.
  - **Caffe Model (`MobileNetSSD_deploy.caffemodel`)**: Contains the pre-trained weights for the MobileNet SSD model.

### Key Components
1. **Prototxt and Caffe Model**:
   - `protopath`: Path to the `.prototxt` file that contains the model architecture.
   - `modelpath`: Path to the pre-trained `.caffemodel` file that contains the model's weights.
   - The `detector` object is created by loading the MobileNet SSD model using `cv2.dnn.readNetFromCaffe()`, which takes both the prototxt and model files as input.

2. **Class Labels (`CLASSES`)**:
   - A list containing object categories that the MobileNet SSD model can recognize. For example, index 15 corresponds to "person".

3. **Main Functionality**:
   - **Video Capture**: The video file (`Cristiano Ronaldo Walks Out For His Second Manchester United Debut At Old Trafford.mp4`) is read using `cv2.VideoCapture()`.
   - **Frame Resizing**: Each video frame is resized using `imutils.resize()` to ensure that the frame dimensions are manageable for processing (width set to 500 pixels in this case).
   - **Blob Creation**: The frame is converted into a blob using `cv2.dnn.blobFromImage()`. This blob is fed into the model for object detection.
   - **Detection**: The blob is passed to the MobileNet SSD model using `detector.setInput(blob)`, and detections are obtained with `detector.forward()`. The output contains the detected objects and their confidence scores.
   - **Bounding Box Drawing**: For each person detection, the bounding box coordinates are extracted, scaled to match the frame size, and a red rectangle is drawn around the detected person.
   - **FPS Calculation**: The frames per second (FPS) of the video processing is calculated and displayed on the video feed to track performance.
   - **Displaying the Video**: The resulting video with bounding boxes around detected persons is displayed in real-time using `cv2.imshow()`.

4. **Error Handling**:
   - If no persons are detected (i.e., the confidence for all detections is below 0.2), the program does not draw any bounding boxes.
   - If the video capture fails or the window cannot be displayed, appropriate error messages may be printed.

### Expected Output
- **Real-time Video**: The video is shown with bounding boxes drawn around any detected persons in each frame.
- **FPS Display**: The FPS is displayed on the video feed to monitor the real-time processing speed.
- **Detection Details**: The console outputs the confidence scores for each detection, indicating how confident the model is in detecting persons.
- **Detection Results**: Multiple persons can be detected in the video, each with a bounding box around them. If no persons are detected, no bounding boxes will be drawn, and the video will proceed without changes.

