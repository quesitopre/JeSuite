from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ReservationPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()
        
        label = QLabel("reservation Page to confirm details")
        self.setStyleSheet("""
            QLabel{
                color: black;
            }
        """)
        layout.addWidget(label)

        self.setLayout(layout)
