# Security camera

The provided code is a simple implementation of a security camera application using OpenCV (cv2) library in Python.
Let's break down the code and understand what it does and how it accomplishes its task.

## Importing necessary libraries:

```python

import cv2
import winsound
```

The code imports the cv2 library for computer vision operations and the winsound library for playing a sound.

Initializing the camera:

```python

camera = cv2.VideoCapture(0)
```

The code creates a VideoCapture object named camera to access the webcam. The parameter 0 indicates that the default camera device should be used.

## Starting the video capture loop:

```python

while camera.isOpened():
```

The code starts a continuous loop that runs as long as the camera is open and available.

   ##Capturing frames:

```python

retrieve, frame1 = camera.read()
retrieve, frame2 = camera.read()
```

Within the loop, the code reads two consecutive frames from the camera using the camera.read() function. The frames are stored in frame1 and frame2 variables.

   ## Calculating frame differences:

```python

differenceFrame = cv2.absdiff(frame1, frame2)
```

The code calculates the absolute difference between frame1 and frame2 using cv2.absdiff(). This operation highlights the areas where there are significant differences between the two frames.

   ## Converting to grayscale:

```python

grayColor = cv2.cvtColor(differenceFrame, cv2.COLOR_BGR2GRAY)
```

The code converts the difference frame (differenceFrame) to grayscale using cv2.cvtColor(). This step simplifies further processing.

    Applying blur:

```python

blur = cv2.GaussianBlur(grayColor, (5, 5), 0)
```

The code applies Gaussian blur to the grayscale image (grayColor) using cv2.GaussianBlur(). This reduces noise and smooths out the image.

   ## Thresholding:

```python

_, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
```

The code applies thresholding to the blurred image (blur) using cv2.threshold(). It converts the image into a binary image, where pixel values above a certain threshold (20 in this case) are set to 255 (white), and below the threshold are set to 0 (black).

   ## Dilation:

```python

dilated = cv2.dilate(thresh, None, iterations=3)
```

The code performs dilation on the thresholded image (thresh) using cv2.dilate(). Dilation expands the white regions in the image, helping to connect broken contours and fill gaps.

    ## Finding contours:

```python

countourse, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
```

The code finds contours in the dilated image (dilated) using cv2.findContours(). Contours are the boundaries of connected components in the image. The function returns the contours in the countourse variable.

   ## Detecting and marking moving objects:

```python

for contour in countourse:
    if cv2.contourArea(contour) < 5000:
        continue
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0))
    winsound.PlaySound("camsound.wav", winsound.SND_ASYNC)
```

    Iterating over contours:
    The code loops over each contour detected in the previous step using the variable countourse.

   ## Filtering contours based on area:
        It checks the area of each contour using cv2.contourArea(contour).
        If the contour's area is less than 5000 pixels, it continues to the next iteration of the loop using the continue statement.
        This filtering step helps eliminate small and insignificant contours that might correspond to noise or irrelevant objects.

   ## Extracting bounding rectangle coordinates:
        If the contour passes the area filter, the code extracts the bounding rectangle coordinates of the contour using cv2.boundingRect(contour).
        The boundingRect function returns the coordinates (x, y) of the top-left corner of the rectangle, as well as its width and height (w, h).
        These coordinates define the position and dimensions of the rectangle that will be drawn around the moving object.

   ## Drawing a rectangle around the object:
        The code draws a rectangle on frame1 using cv2.rectangle().
        The rectangle's coordinates and dimensions are determined by the previously extracted values (x, y, w, h).
        The color of the rectangle is specified as (255, 0, 0), representing blue in BGR format.

   ## Playing a sound:
        After drawing the rectangle, the code plays a sound file named "camsound.wav" using winsound.PlaySound().
        The winsound.SND_ASYNC flag is used to play the sound asynchronously, allowing the code to continue execution without waiting for the sound to finish.

Overall, this section of the code iterates through the detected contours, filters them based on their area, draws bounding rectangles around significant contours, and plays a sound to alert the presence of moving objects in the frame.
