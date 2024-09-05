from flirpy.camera.lepton import Lepton
import numpy as np
import cv2

TEMP_MIN = 60.0
TEMP_MAX = 0.0

with Lepton() as camera:
    while True:
        img = camera.grab()
        img = img/100.0 - 273.15
    
        img = 255.0*(img - TEMP_MIN)/(TEMP_MAX - TEMP_MIN)
        img = img.astype(np.uint8)
        
        img_col = cv2.applyColorMap(img.astype(np.uint8), cv2.COLORMAP_INFERNO)
        
        img = cv2.resize(img_col, (480, 360))
        cv2.imshow('Lepton', img.astype(np.uint8))

        if cv2.waitKey(1) == 27:
            break  # esc to quit
        
cv2.destroyAllWindows()