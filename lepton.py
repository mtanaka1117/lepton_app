from flirpy.camera.lepton import Lepton
import numpy as np
import cv2

with Lepton() as camera:
    while True:
        img = camera.grab().astype(np.float32)

        # Rescale to 8 bit
        img = 255*(img - img.min())/(img.max()-img.min())
        
        # Apply colourmap - try COLORMAP_JET if INFERNO doesn't work.
        # You can also try PLASMA or MAGMA
        img_col = cv2.applyColorMap(img.astype(np.uint8), cv2.COLORMAP_INFERNO)
        
        img_col = cv2.resize(img_col, (480, 360))
        cv2.imshow('Boson', img_col)

        if cv2.waitKey(1) == 27:
            break  # esc to quit
        
cv2.destroyAllWindows()