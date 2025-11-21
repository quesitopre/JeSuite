from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class ShoppingCartPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    '''
    Summary: Initializes the UI for the shoppingCart Page

    Params: None

    Returns: None
    '''
    def initUI(self):
        layout = QVBoxLayout()
        
        label = QLabel("shoppingCart Page to confirm details")
        self.setStyleSheet("""
            QLabel{
                color: black;
            }
        """)
        
        self.button = QPushButton("Go to reservation page")
        self.button.clicked.connect(self.go_to_reservation)

        layout.addWidget(label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    '''
    Summary: Function that goes to reservation page

    Params: None

    Returns: None
    '''
    def go_to_reservation(self):
        self.stacked_widget.setCurrentIndex(3)
