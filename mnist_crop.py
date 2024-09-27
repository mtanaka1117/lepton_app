import cv2
import numpy as np
import os
import re

PATH = "./img/4/20240926_124118962.dat"

threshold = 25.8

with open(PATH, 'rb') as f:
    img_binary = f.read()
img = np.frombuffer(img_binary, dtype=np.uint16).reshape([120, 160])/100.0 - 273.15
img = np.where(img > threshold, 255, 0).astype(np.uint8)

mask = np.zeros((120, 160), dtype=np.uint8)
mask[10:120, 10:130] = 255

img = cv2.medianBlur(img, 3) # filtering
img = cv2.dilate(img, (5,5), iterations=2)
img = cv2.bitwise_and(img, mask)

resize = cv2.resize(img, (28, 28))
match = re.search(r'./img/(\d)/(\d{8}_\d{9})\.dat', PATH)

if match:
    _path = f'{match.group(1)}/{match.group(2)}'
    os.makedirs(os.path.join('./test/', match.group(1)), exist_ok=True)
    output_path = os.path.join('./test/', _path + '.jpg')

cv2.imwrite(output_path, resize)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
