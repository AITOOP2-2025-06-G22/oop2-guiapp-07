import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLabel
)
from PySide6.QtCore import Slot

# 【追加・修正】start_capture.pyからstart_capture関数をインポート
# 注: start_capture.pyがカレントディレクトリにあると仮定します。
try:
    from src.start_capture import start_capture
except ImportError:
    # インポート失敗時のフォールバック処理（例: エラーメッセージ）
    print("Error: Could not import 'start_capture' from 'start_capture.py'.")
    # 代わりに何もしないダミー関数を定義するなど



class ImageViewerApp(QMainWindow):
    """
    GUIアプリケーションのメインウィンドウ（ビュー）を構築するクラス。
    機能（モデル）との紐づけは行わず、見た目とボタンの配置のみを担当する。
    """
    def __init__(self):
        super().__init__()

        # ウィンドウタイトルの設定
        self.setWindowTitle("画像処理プログラム")
        self.resize(600, 400)

        # UI（ユーザーインターフェース）の構築
        self._setup_ui()

    def _setup_ui(self):
        """
        GUIの部品（ボタン、レイアウトなど）を作成し、配置する。
        """

        # 1. メインウィジェットとレイアウトの設定
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # --- 2. ボタンの作成と配置 ---

        # 2-1. 撮影/処理ボタン
        self.capture_button = QPushButton("撮影開始")
        # 【重要】他のメンバーが機能をここに接続します
        self.capture_button.clicked.connect(self._on_capture_clicked)


        # 撮影ボタンを配置
        self.capture_button.setFixedHeight(60)
        main_layout.addWidget(self.capture_button)


        # 操作説明ラベル
        self.setumei_label = QLabel("撮影ボタンを押して画像処理を開始します。\nQボタンを押すと撮影して加工します。\nもう一度Qボタンを押すと終了します。")
        main_layout.addWidget(self.setumei_label)


    @Slot()
    def _on_capture_clicked(self):

        print("撮影/画像処理ボタンが押されました (Model処理を開始)")
        # 【修正箇所】start_capture.pyの関数を呼び出す
        try:
            start_capture()
            print("画像処理が完了しました。")
        except Exception as e:
            print(f"画像処理中にエラーが発生しました: {e}")

def main():
    """
    アプリケーションを実行するメイン関数
    """
    app = QApplication(sys.argv)
    window = ImageViewerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()