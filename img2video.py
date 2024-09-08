import glob
import cv2
from more_itertools import peekable

path = "./img/wall/*.jpg"
file_list = peekable(sorted(glob.iglob(path)))

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter('wall.mp4',fourcc, 10, (160, 120))

for i in file_list:
    img = cv2.imread(i)
    video.write(img)
    
video.release()