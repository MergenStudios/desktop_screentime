import sys
from qt_core import *
from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loader = QUiLoader()
        self.ui = loader.load("ui_files/main.ui")

        self.setCentralWidget(self.ui)
        
def run_ui():
    app = QApplication(sys.argv)
    window = MainWindow()

    apply_stylesheet(app, "dark_teal.xml")

    window.show()
    app.exec()


if __name__ == "__window__":
    run_ui()