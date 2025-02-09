import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True: 
    _, frame = video.read()

    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameBlurred = cv2.GaussianBlur(frameGray, (5, 5), 0)
    frameEdges = cv2.Canny(frameBlurred, 50, 150) 
    contours, _ = cv2.findContours(frameEdges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue

        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        x, y, w, h = cv2.boundingRect(approx)

        if len(approx) == 3:
            shape_name = "Triangle"
        elif len(approx) == 4:
            aspect_ratio = w / float(h)
            shape_name = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"
        elif len(approx) == 5:
            shape_name = "Pentagon"
        elif len(approx) == 6:
            shape_name = "Hexagon"
        else:
            shape_name = "Circle"

        cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
        cv2.putText(frame, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Video Shapes Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    

video.release()
cv2.destroyAllWindows()


    