import os
import sys

from PIL import Image
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel, QVBoxLayout, QListWidget, QComboBox


class ImageConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Converter (PNG ↔ JPG)')
        self.setGeometry(100, 100, 500, 450)

        self.label = QLabel('Select a folder containing images', self)
        self.label.setStyleSheet("font-size: 14px;")

        self.list_widget = QListWidget(self)  # 변환된 파일 목록 표시

        self.btn_select_folder = QPushButton('Select Folder', self)
        self.btn_select_folder.clicked.connect(self.select_folder)

        self.combo_format = QComboBox(self)
        self.combo_format.addItems(["Convert to JPG", "Convert to PNG"])

        self.btn_convert = QPushButton('Convert Images', self)
        self.btn_convert.clicked.connect(self.convert_images)
        self.btn_convert.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.list_widget)
        layout.addWidget(self.btn_select_folder)
        layout.addWidget(self.combo_format)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)
        self.folder_path = ""

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")

        if folder_path:
            self.folder_path = folder_path
            self.label.setText(f"Selected Folder: {os.path.basename(folder_path)}")

            # 이미지 파일 목록 표시
            self.list_widget.clear()
            image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
            if not image_files:
                self.list_widget.addItem("No image files found in the folder.")
                self.btn_convert.setEnabled(False)
            else:
                self.list_widget.addItems(image_files)
                self.btn_convert.setEnabled(True)

    def convert_images(self):
        if not self.folder_path:
            return

        image_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

        if not image_files:
            self.label.setText("No image files found.")
            return

        converted_files = []
        target_format = self.combo_format.currentText()

        for file in image_files:
            image_path = os.path.join(self.folder_path, file)

            # 변환 대상에 맞는 확장자 설정
            if target_format == "Convert to JPG":
                if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
                    continue  # 이미 JPG인 파일은 변환하지 않음
                new_path = image_path.rsplit(".", 1)[0] + ".jpg"
                img = Image.open(image_path)
                img.convert("RGB").save(new_path, "JPEG")
            elif target_format == "Convert to PNG":
                if file.lower().endswith(".png"):
                    continue  # 이미 PNG인 파일은 변환하지 않음
                new_path = image_path.rsplit(".", 1)[0] + ".png"
                img = Image.open(image_path)
                img.save(new_path, "PNG")

            converted_files.append(new_path)

        self.label.setText(f"Converted {len(converted_files)} files.")
        self.list_widget.clear()
        self.list_widget.addItems([os.path.basename(f) for f in converted_files])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageConverter()
    window.show()
    sys.exit(app.exec())
