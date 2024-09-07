import cv2
# from loguru import logger
import datetime as dt
import os

cap = cv2.VideoCapture(1) #wseb camera
FRAME_ID = 0

# if not cap.isOpened():
#     logger.error("Webカメラが開けませんでした。")
#     cap.release()
#     return False

FOLDER = './img/'

while True: #カメラから画像を取得してファイルに書き込むことを繰り返す
    # カメラから映像を取得
    ret, frame = cap.read() #画像の取得が成功したかどうかの結果取得(True成功/Fales失敗)
    now = dt.datetime.now().strftime("%Y%m%d_%H%M%S%f")[:-3]

    output_path = os.path.join(FOLDER, now + '.jpg')
    if ret:
        cv2.imwrite(output_path, frame)
        frame = cv2.resize(frame,(640,480))
        cv2.imshow('Lepton', frame)

        if cv2.waitKey(1) == 27:
            break  # esc to quit
        