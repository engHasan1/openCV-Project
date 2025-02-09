# Face, Shape, and Text Recognition Projects

Welcome to the collection of face, geometric shape, and text recognition projects using the OpenCV library. These projects aim to explore computer vision techniques and their practical applications.

## 1. Face Recognition (FaceRecognition.py)

This project uses the OpenCV library to detect faces in live video. It employs the Haar Cascade classifier to identify faces and displays the frame with rectangles around the detected faces.

### How to Use:
1. Ensure you have the OpenCV library installed.
2. Run the program using Python.
3. Press 'q' to exit the video.

## 2. Geometric Shape Recognition (RecognizingGeoShapes.py)

This project detects geometric shapes in live video. It uses the Canny algorithm for edge detection and identifies shapes such as triangles, squares, rectangles, and circles.

### How to Use:
1. Ensure you have the OpenCV and NumPy libraries installed.
2. Run the program using Python.
3. Press 'q' to exit the video.

## 3. Text Recognition (TextRecognition.py)

This project utilizes the Tesseract OCR library to extract text from live video. The frame is converted to grayscale, and Gaussian Blur is applied before passing the image to Tesseract for text extraction.

### How to Use:
1. Ensure you have the OpenCV and pytesseract libraries installed.
2. Install Tesseract OCR on your machine.
3. Run the program using Python.
4. Press 'q' to exit the video.

## Requirements

- Python 3.x
- OpenCV
- NumPy
- pytesseract (for the third project)
- Tesseract OCR (for the third project)

## Installation

You can install the required libraries using pip:
