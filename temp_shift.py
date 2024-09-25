import glob
import cv2
import numpy as np
from more_itertools import peekable
import os
import matplotlib.pyplot as plt
# import japanize_matplotlib
import pandas as pd


coord = []
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coord.append([y, x])
        print(y, x)
        cv2.destroyAllWindows()

def get_coord(path):
    img = cv2.imread(path)
    cv2.imshow('img', img)
    cv2.setMouseCallback('img', onMouse)
    cv2.waitKey(0)

path = "./img/cloth_wall/20240909_154733398.jpg"

get_coord(path)
coord_x, coord_y = coord[0]

DIR_PATH = path[:-22] + "*.dat"
file_list = peekable(sorted(glob.iglob(DIR_PATH)))

material = []

for i, file in enumerate(file_list):
    with open(file, "rb") as f:
        img_binary = f.read()
        data = np.frombuffer(img_binary, dtype=np.uint16).reshape([120, 160])/100.0 - 273.15
        if data[coord_x][coord_y] < 40 and data[coord_x][coord_y] > 0:
            material.append(data[coord_x][coord_y])

fig = plt.figure()
# material = pd.Series(material)
plt.plot(material)
plt.xlabel("frame count")
plt.ylabel("temperature")
plt.show()
