from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import pydoc

class ShoppingCartPage(QWidget):
    '''
    Represents the shopping cart page where users can review selected rooms 
    and proceed to the reservation page.
    '''
    def __init__(self, stacked_widget):
        '''
        Initializes the ShoppingCartPage and sets up the UI components.

        Parameters:
            stacked_widget (QStackedWidget): Used to navigate between pages.

        Returns:
            None
        '''
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        '''
        Sets up the UI for the shopping cart page, including a label 
        and a button to go to the reservation page.

        Parameters:
            None

        Returns:
            None
        '''
        layout = QVBoxLayout()
        
        label = QLabel("shoppingCart Page to confirm details")
        self.setStyleSheet("""
            QLabel{
                color: black;
            }
            QPushButton {
                background-color: #8c6d3d;
            }
            QComboBox {
                background-color: #8c6d3d;
            }
        """)
        
        self.button = QPushButton("Go to reservation page")
        self.button.clicked.connect(self.go_to_reservation)

        layout.addWidget(label)
        layout.addWidget(self.button)

        self.setLayout(layout)
    
    def go_to_reservation(self):
        '''
        Navigates to the reservation page by changing the stacked widget index.

        Parameters:
            None

        Returns:
            None
        '''
        self.stacked_widget.setCurrentIndex(3)

pydoc.writedoc("shoppingCartPage")

