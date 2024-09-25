import cv2
import numpy as np
import os
import re
import glob


def centralize_and_resize(image_path, output_size=(28, 28), min_digit_size=5):
    # 画像を読み込み
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # dilate_img = cv2.dilate(img, (3,3), iterations=5)

    # 輪郭を取得
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contours) == 0:
        return img
        
    largest_contour = max(contours, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(largest_contour)
    
    # 数字の部分を切り抜く
    digit = img[y:y+h, x:x+w]
    
    # 数字が小さい場合に拡大
    if w < min_digit_size or h < min_digit_size:
        digit = cv2.resize(digit, (28, 28), interpolation=cv2.INTER_AREA)
    
    # 新しい空のキャンバスを作成（中央に配置するため）
    canvas = np.zeros(output_size, dtype=np.uint8)
    
    # 数字を中央に配置するための座標を計算
    h, w = digit.shape
    x_offset = (output_size[1] - w) // 2
    y_offset = (output_size[0] - h) // 2
    
    # 数字をキャンバスに配置
    canvas[y_offset:y_offset+h, x_offset:x_offset+w] = digit
    
    return canvas


INPUT_DIR = './test_dataset/6'
OUTPUT_DIR = './test/6/'

os.makedirs(OUTPUT_DIR, exist_ok=True)

for img in glob.glob(INPUT_DIR + '/*.jpg'):
    resized_img = centralize_and_resize(img)
    
    match = re.search(r'./test_dataset/(\d)[\\/](\d{8}_\d{9})\.jpg', img)
    if match:
        _path = f'{match.group(2)}'
        output_path = os.path.join(OUTPUT_DIR, _path + '.jpg')
    else:
        print('Not match')
        
    cv2.imwrite(output_path, resized_img)

