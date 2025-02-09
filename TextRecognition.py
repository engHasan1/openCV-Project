import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd=r'c:\Program Files\Tesseract-OCR\tesseract.exe'

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()

    if not ret:
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    blurr=cv2.GaussianBlur(gray,(5,5),0)

    text=pytesseract.image_to_string(blurr)

    print(text)

    cv2.putText(frame, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Video Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()