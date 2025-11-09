import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class RoomSelectionPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        main_layout = QVBoxLayout()

        next_btn = QPushButton("Continue to Reservation Form")
        next_btn.clicked.connect(self.go_to_reservation_form)
        main_layout.addWidget(next_btn)

        self.setLayout(main_layout)

    def go_to_reservation_form(self):
        self.stacked_widget.setCurrentIndex(2)