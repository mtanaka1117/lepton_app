from flirpy.camera.lepton import Lepton
import numpy as np
import cv2
import datetime as dt

camera = Lepton()
cap = camera.setup_video()

while True:
    ret, frame = cap.read() #画像の取得が成功したかどうかの結果取得(True成功/Fales失敗)
    now = dt.datetime.now().strftime("%Y%m%d_%H%M%S%f")[:-3]

    if ret:
        cv2.imwrite('./img/{}.jpg'.format(now), frame)
        frame = cv2.resize(frame,(640,480))
        cv2.imshow('Lepton', frame)

        if cv2.waitKey(1) == 27:
            break  # esc to quit
        