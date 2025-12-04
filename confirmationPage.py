from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ConfirmationPage(QWidget):
    def __init__(self, stacked_widget = None):
        super().__init__()
        self.stacked_widget = stacked_widget

        self.initUI()


    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        # Container card box
        #box = QFrame()
        #box.setObjectName("box")
        #box.setStyleSheet("""
        #    QFrame#box {
        #        background: #ffffff;
        #        border-radius: 20px;
        #        padding: 30px 40px;
        #        border: 1px solid #e5e5e5;
        #    }
        #""")

        #label = QLabel(
        # "Thank you for booking with us!\n" 
        # "Your reservation has been successfully confirmed.\n"
        # "A detailed confirmation receipt has been sent to your email.\n"
        # "We look forward to welcoming you!"
        #)
        #self.setStyleSheet("""
        #    QLabel{
        #        color: black;
        #    }
        #""")
        #layout.addWidget(label)
        #self.setLayout(layout)

        box_layout = QVBoxLayout()
        box_layout.setSpacing(18)
        box_layout.setAlignment(Qt.AlignCenter)

        # Title
        self.title = QLabel("🎉 Thank you for booking with us! 🎉")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel {
                font-size: 24px;
                font-weight: bold;
                color: #2a2a2a;
            }
        """)

        # Subtitle(message)
        self.message = QLabel(
            "Your reservation has been successfully confirmed.\n"
            "A detailed confirmation receipt has been sent to your email.\n"
            "We look forward to welcoming you!"
        )
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #555555;
                line-height: 1.4;
            }
        """)

        # Button
        self.done_button = QPushButton("Return to Home")
        self.done_button.setFixedHeight(40)
        self.done_button.setStyleSheet("""
            QLabel {
                color: black;          
            }
            QPushButton {
                background-color: #8c6d3d;
            }
            QComboBox {
                background-color: #8c6d3d;
            }
        """)
        self.done_button.clicked.connect(self.go_to_home_page)

        # Add widgets to card box
        box_layout.addWidget(self.title)
        box_layout.addWidget(self.message)
        box_layout.addSpacing(10)
        box_layout.addWidget(self.done_button)

        #layout.addWidget(box)

        layout.addLayout(box_layout)

        self.setLayout(layout)

    def go_to_home_page(self):
            self.stacked_widget.setCurrentIndex(0)
