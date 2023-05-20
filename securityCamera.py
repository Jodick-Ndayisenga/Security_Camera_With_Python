import cv2
import winsound

camera = cv2.VideoCapture(0)

while camera.isOpened():

    retrieve, frame1 = camera.read()

    retrieve, frame2 = camera.read()

    differenceFrame = cv2.absdiff(frame1, frame2)

    grayColor = cv2.cvtColor(differenceFrame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(grayColor, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh, None, iterations=3)

    countourse, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for coutour in countourse:
        if cv2.contourArea(coutour) < 5000:
            continue

        x, y, w, h = cv2.boundingRect(coutour)

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (255, 0, 0))

        winsound.PlaySound("camsound.wav", winsound.SND_ASYNC)

    if cv2.waitKey(10) == ord("q"):
        break

    cv2.imshow("Security Camera", frame1)
