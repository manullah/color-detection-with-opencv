import cv2
import numpy as np
from PIL import Image


def try_one(frame):
    # Tentukan rentang warna merah dalam format HSV
    # Option 1
    lower_red = cv2.inRange(hsv, (0, 50, 20), (5, 255, 255))
    upper_red = cv2.inRange(hsv, (175, 50, 20), (180, 255, 255))
    # Option 2
    # lower_red = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
    # upper_red = cv2.inRange(hsv, (160, 100, 100), (180, 255, 255))
    # Option 3
    # lower_red = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
    # upper_red = cv2.inRange(hsv, (160, 100, 100), (179, 255, 255))

    # Buat mask yang hanya mempertahankan warna merah
    mask = cv2.bitwise_or(lower_red, upper_red)

    # Temukan kontur objek dalam mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Gambar kotak pada setiap konturnya
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5)


################################################################

# Inisialisasi image
frame = cv2.imread("./2.jpeg")

# Konversi frame ke format HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

try_one(frame)

# Simpan hasil
cv2.imwrite("./result.jpeg", frame)

# Tampilkan hasil
# cv2.imshow("Color Detection", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
