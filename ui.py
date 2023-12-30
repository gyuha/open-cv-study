import sys

import cv2
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class CardDetectorUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI 설정
        self.setWindowTitle("Card Detector")
        self.setGeometry(100, 100, 800, 600)

        # 레이아웃 및 위젯 설정
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # 이미지 라벨
        self.image_label = QLabel()
        self.image_label.setFixedSize(640, 480)
        layout.addWidget(self.image_label)

        # 이미지 선택 버튼
        self.btn_select_image = QPushButton("Select Image")
        self.btn_select_image.clicked.connect(self.select_image)
        layout.addWidget(self.btn_select_image)

        # 카드 인식 버튼
        self.btn_detect_card = QPushButton("Detect Top Card")
        self.btn_detect_card.clicked.connect(self.detect_top_card)
        layout.addWidget(self.btn_detect_card)

    def select_image(self):
        # 이미지 선택 다이얼로그 열기
        fname, _ = QFileDialog.getOpenFileName(self, "Open file", "./", "Image files (*.jpg *.png)")
        if fname:
            # 이미지 라벨에 표시
            pixmap = QPixmap(fname)
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            )
            self.current_image_path = fname

    def detect_top_card(self):
        if hasattr(self, "current_image_path"):
            # 이미지에서 카드 인식
            image = cv2.imread(self.current_image_path)
            # ... 여기에 카드 인식 코드를 넣습니다 ...
            # 예시로, 인식된 카드 영역에 빨간색 사각형을 그리는 코드
            cv2.rectangle(image, (50, 50), (200, 200), (0, 0, 255), 2)
            # OpenCV 이미지를 QPixmap으로 변환
            height, width, channel = image.shape
            bytes_per_line = 3 * width
            q_img = QImage(image.data, width, height, bytes_per_line, QImage.Format.Format_BGR888)
            pixmap = QPixmap.fromImage(q_img)
            # 이미지 라벨에 표시
            self.image_label.setPixmap(
                pixmap.scaled(self.image_label.size(), aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
            )


# 앱 실행
app = QApplication(sys.argv)
window = CardDetectorUI()
window.show()
sys.exit(app.exec())
