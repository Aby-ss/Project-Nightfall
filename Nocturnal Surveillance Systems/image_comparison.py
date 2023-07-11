import cv2
import face_recognition

from rich import box
from rich.panel import Panel
from rich.console import Console

console = Console()

img = cv2.imread("Messi1.webp")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

img2 = cv2.imread("images/Messi.webp")
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)
console.log(Panel.fit(f"Result: {result}", border_style="Bold green", box = box.SQUARE))

cv2.imshow("Img", img)
cv2.imshow("Img 2", img2)
cv2.waitKey(0)