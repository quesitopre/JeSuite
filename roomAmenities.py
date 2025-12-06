from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class RoomAmenities(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setObjectName("RoomAmenities")
        self.setStyleSheet("""
            #RoomAmenities {
                border: 1px solid #000000;
                border-radius: 12px;
            }
            QLabel {
                font-size: 15px;
                color: black;    
            }
        """)

        main = QVBoxLayout()
        label = QLabel("Amenities")
        label.setAlignment(Qt.AlignCenter)
        main.addWidget(label)

        layout = QHBoxLayout()

        left = QVBoxLayout()
        center = QVBoxLayout()
        right = QVBoxLayout()

        a1 = QLabel(f"* Refrigerator")
        a2 = QLabel(f"* Stove")
        a3 = QLabel(f"* Microwave")
        a4 = QLabel(f"* TV")
        a5 = QLabel(f"* Pool")
        a6 = QLabel(f"* Fitness Center")
        a7 = QLabel(f"* EV Charging")
        a8 = QLabel(f"* Free Parking")
        a9 = QLabel(f"* Free Breakfast")
        a10 = QLabel(f"* No Pets Allowed")
        a11 = QLabel(f"* No Smoking Allowed")


        left.addWidget(a1)
        left.addWidget(a2)
        left.addWidget(a3)
        left.addWidget(a4)
        left.setAlignment(Qt.AlignCenter)

        center.addWidget(a5)
        center.addWidget(a6)
        center.addWidget(a7)
        center.addWidget(a8)
        center.setAlignment(Qt.AlignCenter)

        right.addWidget(a9)
        right.addWidget(a10)
        right.addWidget(a11)
        right.setAlignment(Qt.AlignCenter)

        layout.addLayout(left)
        layout.addLayout(center)
        layout.addLayout(right)
        #layout.setAlignment(Qt.AlignCenter)

        main.addLayout(layout)

        self.setLayout(main)