import numpy as np
import cv2

from rich.panel import Panel
from rich import box

from rich.traceback import install
install(show_locals=True)

img = cv2.VideoCapture(0)

ret, frame = img.read()
cv2.imshow("Camera feed", frame)

blur = cv2.GaussianBlur(img, (7, 7), 2)
h, w = img.shape[:2]

# Binarize gradient

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
gradient = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)

lowerb = np.array([0, 0, 0])
upperb = np.array([15, 15, 15])
binary = cv2.inRange(gradient, lowerb, upperb)
cv2.imshow('Binarized gradient', binary)

image = binary
k = cv2.waitKey(0)

if( k == ord('g') ):
  cv2.imwrite('Detected Image', image )
  print(Panel("Image saved", box = box.SQUARE, border_style = "Bold Red"))
  img.release()
  cv2.destroyAllWindows()