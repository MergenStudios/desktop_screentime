import sys, os
from qt_core import *

from qt_material import apply_stylesheet

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()

        self.ui = loader.load(f"{BASE_DIR}/ui_files/main.ui")
        self.setCentralWidget(self.ui) 


def run_ui():
    app = QApplication(sys.argv)
    window = MainWindow()

    apply_stylesheet(app, theme="dark_teal.xml")

    window.show()

    center = QScreen.availableGeometry(QApplication.primaryScreen()).center()
    geo = window.frameGeometry()
    geo.moveCenter(center)
    window.move(geo.topLeft())

    app.exec()


if __name__ == "__main__":
    run_ui()