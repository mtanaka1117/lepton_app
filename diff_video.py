import glob
import cv2
from more_itertools import peekable

path = "./img/wall/*.jpg"
file_list = peekable(sorted(glob.iglob(path)))

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter('wall_diff.mp4',fourcc, 10, (160, 120), isColor=False)

bg_img = cv2.imread(next(file_list))
bg_img = cv2.GaussianBlur(bg_img, (5, 5), 0)

for i in file_list:
    img = cv2.imread(i)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    
    diff = cv2.absdiff(bg_img, img)
    diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, img_th = cv2.threshold(diff,3,255,cv2.THRESH_BINARY)
    
    video.write(img_th)
    
video.release()