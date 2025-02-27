import os
import sys

from PIL import Image
from PyQt6.QtWidgets import QWidget, QPushButton, QFileDialog, QLabel, QVBoxLayout, QListWidget, QApplication


class ImageConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PNG to JPG Converter (Folder Mode)')
        self.setGeometry(100, 100, 500, 400)

        self.label = QLabel('Select a folder containing PNG files', self)
        self.label.setStyleSheet("font-size: 14px;")

        self.list_widget = QListWidget(self)  # 변환된 파일 목록 표시

        self.btn_select_folder = QPushButton('Select Folder', self)
        self.btn_select_folder.clicked.connect(self.select_folder)

        self.btn_convert = QPushButton('Convert All PNGs', self)
        self.btn_convert.clicked.connect(self.convert_images)
        self.btn_convert.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.btn_select_folder)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)

        self.folder_path = ""

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")

        if folder_path:
            self.folder_path = folder_path
            self.label.setText(f"Selected Folder: {os.path.basename(folder_path)}")

            # PNG 파일 목록 표시
            self.list_widget.clear()
            png_files = [f for f in os.listdir(folder_path) if f.lower().endswith(".png")]
            if not png_files:
                self.list_widget.addItem("No PNG files found in the folder.")
                self.btn_convert.setEnabled(False)
            else:
                self.list_widget.addItems(png_files)
                self.btn_convert.setEnabled(True)

    def convert_images(self):
        if not self.folder_path:
            return

        png_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith(".png")]

        if not png_files:
            self.label.setText("No PNG files found.")
            return

        converted_files = []
        for file in png_files:
            png_path = os.path.join(self.folder_path, file)
            jpg_path = png_path.replace(".png", ".jpg")

            img = Image.open(png_path)
            img.convert("RGB").save(jpg_path, "JPEG")

            converted_files.append(jpg_path)

        self.label.setText(f"Converted {len(converted_files)} PNG files to JPG.")
        self.list_widget.clear()
        self.list_widget.addItems([os.path.basename(f) for f in converted_files])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageConverter()
    window.show()
    sys.exit(app.exec())
