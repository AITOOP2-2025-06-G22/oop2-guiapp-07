import cv2
from my_module.K24128.lecture05_camera_image_capture import MyVideoCapture
from src.edit_camera import edit_camera_image

def start_capture():
    """
    Webカメラから映像を取得し、中心にターゲットマークを描画して表示・保存する関数。

    Notes:
        映像は"output_images/captured_image.png"に保存される。
    """
    # カメラキャプチャ実行（ファイル保存はしない）
    app = MyVideoCapture()
    app.run()

    # メモリ上のキャプチャ画像を取得
    capture_img: cv2.Mat = app.get_img()

    if capture_img is None:
        raise ValueError("カメラ画像が取得できませんでした。")
    
    # ファイルの出力
    cv2.imwrite("output_images/captured_image.png", capture_img)

    edit_camera_image()
