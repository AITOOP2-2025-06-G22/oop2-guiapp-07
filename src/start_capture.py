import cv2
from my_module.K24128.lecture05_camera_image_capture import MyVideoCapture

def start_capture():
    # カメラキャプチャ実行（ファイル保存はしない）
    app = MyVideoCapture()
    app.run()

    # メモリ上のキャプチャ画像を取得
    capture_img: cv2.Mat = app.get_img()

    if capture_img is None:
        raise ValueError("カメラ画像が取得できませんでした。")
    
    # ファイルの出力
    cv2.imwrite("output_images/captured_image.png", capture_img)
