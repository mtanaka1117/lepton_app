import glob
import cv2
from more_itertools import peekable
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--path")
args = parser.parse_args()

PATH = os.path.join(args.path, '*.jpg')
file_list = peekable(sorted(glob.iglob(PATH)))

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter('cloth_wall_cold.mp4',fourcc, 10, (160, 120))

for i in file_list:
    img = cv2.imread(i)
    video.write(img)
    
video.release()