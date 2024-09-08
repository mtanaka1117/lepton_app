import glob
import cv2
import numpy as np
from more_itertools import peekable
import os
import matplotlib.pyplot as plt
# import japanize_matplotlib
from scipy.stats import norm
import statistics
import math
import pandas as pd
import argparse

coord_x = 0
coord_y = 0
def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # x, y = x//3, y//3
        coord_x = y
        cood_y = x
        print(x, y)
        cv2.destroyAllWindows()

def get_coord(path):
    img = cv2.imread(path)
    # img = cv2.resize(img, (480, 360))
    cv2.imshow('img', img)
    cv2.setMouseCallback('img', onMouse)
    cv2.waitKey(0)


path = "./img/wall/20240908_202435731.jpg"
get_coord(path)


DIR_PATH = './img/'

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--material")
args = parser.parse_args()

path = os.path.join(DIR_PATH, args.material, "*.dat")
file_list = peekable(sorted(glob.iglob(path)))

material = []

for i, file in enumerate(file_list):
    with open(file, "rb") as f:
        img_binary = f.read()
        data = np.frombuffer(img_binary, dtype=np.uint16).reshape([120, 160])/100 - 273.15
        material.append(data[coord_x][coord_y])

fig = plt.figure()
plt.plot(material)
plt.show()
