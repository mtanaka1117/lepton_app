import numpy as np
from PIL import Image
import os
from more_itertools import peekable
import glob
import pandas as pd

DIR_PATH = './img/wall/*.dat'

MIN_TEMP = 20.0
MAX_TEMP = 40.0

file_list = peekable(sorted(glob.iglob(DIR_PATH)))

for file in file_list:
    with open(file, 'rb') as f:
        img_binary = f.read()
    data = np.frombuffer(img_binary, dtype=np.uint16).reshape([120, 160])/100.0-273.15
    data = 255*(data - MIN_TEMP)/(MAX_TEMP - MIN_TEMP)
    # data = np.frombuffer(img_binary, dtype=np.uint16).reshape([120, 160]).astype(np.float32)
    # data = 255*(data - data.min())/(data.max()-data.min())
    image = Image.fromarray(data.astype(np.uint8))
    image.save(file[:-4] + '.jpg', 'JPEG')

