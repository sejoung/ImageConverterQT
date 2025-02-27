import sys

from PyQt6.QtWidgets import QApplication

from image.Image_converter import ImageConverter


def test_run():
    app = QApplication(sys.argv)
    window = ImageConverter()
    window.show()
    sys.exit(app.exec())
