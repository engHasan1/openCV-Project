import cv2


FaceCasCade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    if not ret:
        break


    grayIm = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    blurrIm = cv2.GaussianBlur(grayIm, (5, 5), 0)


    faces = FaceCasCade.detectMultiScale(blurrIm, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)


    cv2.imshow('Face Detection', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()
cv2.destroyAllWindows()
