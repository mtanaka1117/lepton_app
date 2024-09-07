from flirpy.camera.lepton import Lepton
import numpy as np
import cv2
import datetime as dt
import os

def raw_to_8bit(data):
    cv2.normalize(data, data, 0, 65535, cv2.NORM_MINMAX)
    np.right_shift(data, 8, data)
    return cv2.cvtColor(np.uint8(data), cv2.COLOR_GRAY2RGB)

SAVE_FLAG = False
TODAY = dt.date.today().strftime("%m%d")
SAVE_DIR = './img/'

os.makedirs(os.path.join(SAVE_DIR, TODAY), exist_ok=True)

with Lepton() as camera:
    while True:
        img = camera.grab() # uint16
        
        now = dt.datetime.now().strftime("%Y%m%d_%H%M%S%f")[:-3]
        with open('./img/{}.dat'.format(now), 'wb') as f:
            f.write(img)
        
        # 16bit to 8bit
        img = raw_to_8bit(img)
        
        img_col = cv2.applyColorMap(img.astype(np.uint8), cv2.COLORMAP_INFERNO)
        img_col = cv2.resize(img_col, (480, 360))
        cv2.imshow('Lepton', img_col.astype(np.uint8))

        if cv2.waitKey(1) == 27:
            break  # esc to quit
        
cv2.destroyAllWindows()