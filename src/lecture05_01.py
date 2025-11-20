import numpy as np
import cv2
from my_module.K24128.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行（ファイル保存はしない）
    app = MyVideoCapture()
    app.run()

    # メモリ上のキャプチャ画像を取得
    capture_img: cv2.Mat = app.get_img()

    if capture_img is None:
        raise ValueError("カメラ画像が取得できませんでした。")

    # 画像をローカル変数に保存
    google_img: cv2.Mat = cv2.imread('images/google.png')

    g_h, g_w, _ = google_img.shape
    c_h, c_w, _ = capture_img.shape

    print(f"google_img: {google_img.shape}")
    print(f"capture_img: {capture_img.shape}")

    # google_img と同じサイズのタイル画像を作成
    tiled_img = np.zeros_like(google_img)

    # グリッド上にキャプチャ画像を貼る（拡大・縮小なし）
    for y in range(0, g_h, c_h):
        for x in range(0, g_w, c_w):
            y_end = min(y + c_h, g_h)
            x_end = min(x + c_w, g_w)
            tiled_img[y:y_end, x:x_end] = capture_img[0:(y_end - y), 0:(x_end - x)]

    # 白い部分を置き換え
    white_mask = np.all(google_img == [255, 255, 255], axis=-1)
    result_img = np.copy(google_img)
    result_img[white_mask] = tiled_img[white_mask]

    # 結果を保存
    cv2.imwrite('output_images/lecture05_01_k24128.png', result_img)


if __name__ == "__main__":
    lecture05_01()
