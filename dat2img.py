import numpy as np
from PIL import Image
import os
from more_itertools import peekable
import glob
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path")
args = parser.parse_args()

PATH = os.path.join(args.path, '*.dat')
file_list = peekable(sorted(glob.iglob(PATH)))

for file in file_list:
    with open(file, 'rb') as f:
        img_binary = f.read()
    data = np.frombuffer(img_binary, dtype=np.uint16).reshape([120, 160]) - 27315
    data = data >> 4
    data = np.clip(data, 0, 255)

    image = Image.fromarray(data.astype(np.uint8))
    image.save(file[:-4] + '.jpg', 'JPEG')

