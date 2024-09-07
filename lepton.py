from flirpy.camera.lepton import Lepton
import numpy as np
import cv2

with Lepton() as camera:
    while True:
        img = camera.grab().astype(np.float32)

        img = 255*(img - img.min())/(img.max()-img.min())
        img_col = cv2.applyColorMap(img.astype(np.uint8), cv2.COLORMAP_INFERNO)
        
        img_col = cv2.resize(img_col, (480, 360))
        cv2.imshow('Lepton', img_col)

        if cv2.waitKey(1) == 27:
            break  # esc to quit
        
cv2.destroyAllWindows()